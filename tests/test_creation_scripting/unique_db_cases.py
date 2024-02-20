import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from src.models.ko_article import KoArticles

pronunciation_dict = {}
articles = KoArticles()
articles.load_all('select * from ko_article group by pronunciation')
for article in articles:
    for i, pronunciation in enumerate(article.pronunciation.split(';;;')):
        if pronunciation not in pronunciation_dict:
            pattern = r'(\|a=[^|}]+)|(\|audio=[^|}]+)' # remove audio files
            stripped_pronunciation = re.sub(pattern, '', pronunciation)
            pattern = r'(\|[^=|}]+)(?=[|}])' # remove Hangul
            hangul_matches = re.findall(pattern, stripped_pronunciation, re.IGNORECASE)
            for hm in hangul_matches:
                stripped_pronunciation = stripped_pronunciation.replace(hm, '')
            pronunciation_dict[stripped_pronunciation] = { "article": article, "original": pronunciation, "index": i }

with open("tests/test_unique_db_cases.py", "w", encoding="utf-8") as f:
    print('''import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestUniqueDBCases(unittest.TestCase):
\tfile = ''

\tdef set_file(self, file):
\t\tself.file = file
''', file=f)
    # Now we need to scrape the actual wiki pages for each to see the results of the original wiki Lua romanization
    # to test ours against.
    for key, value in pronunciation_dict.items():
        url = "https://en.wiktionary.org/wiki/" + quote(value["article"].page_title)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        korean_header = soup.find('span', id="Korean")
        # I found this looking for this to be the most consistent way of finding pronunciations, as the labeling
        # of headers was not consistent
        sk_standard_link = korean_header.find_next('a', {"title":'w:South Korean standard language'}, text="SK Standard")
        ipa_span = sk_standard_link.find_next('span', class_='IPA')
        for i in range(0, value["index"] + 1):
            if i != 0:
                sk_standard_link = ipa_span.find_next('a', {"title":'w:South Korean standard language'}, text="SK Standard")
                ipa_span = sk_standard_link.find_next('span', class_='IPA')
            # find the pronunciation span with the correct index
            if i != value["index"]:
                continue
            ph_li = ipa_span.find_next('li', class_='ko-pron__ph')
            ph_text = ph_li.find_next('span', class_="Kore").text.strip('[]')
            romanizations_table = ipa_span.find_next('table', class_="ko-pron")
            rr = romanizations_table.find_next("td", class_="IPA")
            rrr = rr.find_next("td", class_="IPA")
            mr = rrr.find_next("td", class_="IPA")
            yc = mr.find_next("td", class_="IPA")
            original_params = value["article"].pronunciation.split(';;;')[value["index"]]
            if not original_params:
                continue # This is probably a redirect page
            for name, expected in zip(["ph", "rr", "rrr", "mr", "yr", "ipa"], [ph_text, rr.text, rrr.text, mr.text, yc.text, ipa_span.text]):
                print(f'''\tdef test_{rr.text.replace(' ', '_').replace("'", "").replace("/", "_")}_{name}(self):\n\t\tself.run_test("{value["article"].page_title}", "{original_params}", "{expected}", "{name}")''', file=f)
        print("", file=f)
    print('''
\tdef run_test(self, hangul, param_string, expected, system_name):
\t\twr = WiktionaryRomanization(hangul, param_string)
\t\tif (self.file):
\t\t\ttry:
\t\t\t\tvalue = wr.romanize_one(system_name)
\t\t\t\tprint(f"{inspect.stack()[1].frame.f_code.co_name}: { 'success' if value == expected else f'fail expected {expected} but received {value}'}", file=self.file)
\t\t\texcept Exception as e:
\t\t\t\tprint(f"{inspect.stack()[1].frame.f_code.co_name}: fail {e}", file=self.file)
\t\telse:
\t\t\tvalue = wr.romanize_one(system_name)
\t\t\tself.assertEqual(value, expected)''', file=f)

