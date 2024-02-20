import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from src.models.ko_article import KoArticles

articles = KoArticles()
articles.load_all("select * from ko_article")
with open("tests/test_all_wiki_articles.py", "w", encoding="utf-8") as f:
    print('''import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestUniqueDBCases(unittest.TestCase):
\tfile = ''

\tdef set_file(self, file):
\t\tself.file = file
''', file=f)
    for article in articles:
        for i, pronunciation in enumerate(article.pronunciation.split(';;;')):
            if not pronunciation:
                continue
            url = "https://en.wiktionary.org/wiki/" + quote(article.page_title)
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, 'html.parser')
            korean_header = soup.find('span', id="Korean")
            # I found this looking for this to be the most consistent way of finding pronunciations, as the labeling
            # of headers was not consistent
            sk_standard_link = korean_header.find_next('a', {"title":'w:South Korean standard language'}, text="SK Standard")
            ipa_span = sk_standard_link.find_next('span', class_='IPA')
            for j in range(0, i + 1):
                if j != 0:
                    sk_standard_link = ipa_span.find_next('a', {"title":'w:South Korean standard language'}, text="SK Standard")
                    ipa_span = sk_standard_link.find_next('span', class_='IPA')
                # find the pronunciation span with the correct index
                if j != i:
                    continue
                ph_li = ipa_span.find_next('li', class_='ko-pron__ph')
                ph_text = ph_li.find_next('span', class_="Kore").text.strip('[]')
                romanizations_table = ipa_span.find_next('table', class_="ko-pron")
                rr = romanizations_table.find_next("td", class_="IPA")
                rrr = rr.find_next("td", class_="IPA")
                mr = rrr.find_next("td", class_="IPA")
                yc = mr.find_next("td", class_="IPA")
                if not pronunciation:
                    continue # This is probably a redirect page
                for name, expected in zip(["ph", "rr", "rrr", "mr", "yr", "ipa"], [ph_text, rr.text, rrr.text, mr.text, yc.text, ipa_span.text]):
                    print(f'''\tdef test_{rr.text.replace(' ', '_').replace("'", "").replace("/", "_")}_{name}{('_' + str(i)) if i > 0 else ''}(self):\n\t\tself.run_test("{article.page_title}", "{pronunciation}", "{expected}", "{name}")''', file=f)
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

