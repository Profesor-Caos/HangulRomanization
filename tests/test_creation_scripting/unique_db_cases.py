import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from src.models.ko_article import KoArticles

pronunciation_dict = {}
articles = KoArticles()
articles.load_all('select * from ko_article group by pronunciation')
for article in articles:
    pattern = r'(\{\{ko-ipa.*?(?=}})\}\})'
    matches = re.findall(pattern, article.pronunciation, re.IGNORECASE)
    trimmed_matches = []
    for match in matches:
        pattern = r'(\|a=[^|}]+)|(\|audio=[^|}]+)' # remove audio files
        new_match = re.sub(pattern, '', match)
        pattern = r'(\|[^=|}]+)(?=[|}])' # remove Hangul
        hangul_matches = re.findall(pattern, new_match, re.IGNORECASE)
        for hm in hangul_matches:
            new_match = new_match.replace(hm, '')
        if new_match not in pronunciation_dict:
            pronunciation_dict[new_match] = { "article": article, "original": match, "index": -1 }

# We need to figure out which instance of {{ko-ipa}} on our page our unique instance corresponds to.
for key, value in pronunciation_dict.items():
    page_text = value["article"].page_text
    pattern = r'({{ko-ipa.*?}})'
    matches = re.findall(pattern, page_text, re.IGNORECASE)
    for i, match in enumerate(matches):
        if (match == value["original"]):
            value["index"] = i
            break
    if (value["index"] == -1):
        raise Exception("something's gone wrong.")

def get_vals_from_pron_span(pronunciation_span):
    ipa_text = pronunciation_span.find_next('span', class_='IPA').text
    ph_li = pronunciation_span.find_next('li', class_='ko-pron__ph')
    ph_text = ph_li.find_next('span', class_="Kore").text.strip('[]')
    romanizations_table = pronunciation_span.find_next('table', class_="ko-pron")
    rr = romanizations_table.find_next("td", class_="IPA")
    rrr = rr.find_next("td", class_="IPA")
    mr = rrr.find_next("td", class_="IPA")
    yc = mr.find_next("td", class_="IPA")
    return (ipa_text, ph_text, rr.text, rrr.text, mr.text, yc.text)

with open("tests/test_unique_db_cases.py", "w", encoding="utf-8") as f:
    print('''import sys
pkg_dir = "C:\\\\Users\\\\Ryan\\\\Source\\\\MachineLearning\\\\HangulRomanization" # obviously hacky, but I just want to get debugging tests working
sys.path.append(pkg_dir)

import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestUniqueDBCases(unittest.TestCase):
''', file=f)
    # Now we need to scrape the actual wiki pages for each to see the results of the original wiki Lua romanization
    # to test ours against.
    for key, value in pronunciation_dict.items():
        url = "https://en.wiktionary.org/wiki/" + quote(value["article"].page_title)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        korean_header = soup.find('span', id="Korean")
        vals = []
        # I found this looking for this to be the most consistent way of finding pronunciations, as the labeling
        # of headers was not consistent
        ipa_span = korean_header.find_next('span', class_='IPA')
        for i in range(0, value["index"] + 1):
            if i != 0:
                ipa_span = ipa_span.find_next('span', class_='IPA')
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
            for name, expected in zip(["ph", "rr", "rrr", "mr", "yr", "ipa"], [ph_text, rr.text, rrr.text, mr.text, yc.text, ipa_span.text]):
                print(f'''\tdef test_{rr.text.replace(' ', '_').replace("'", "").replace("/", "_")}_{name}(self):\n\t\tself.run_test("{value["article"].page_title}", "{key}", "{expected}", "{name}")''', file=f)
        print("", file=f)
    print('''
\tdef run_test(self, hangul, param_string, expected, system_name):
\t\twr = WiktionaryRomanization(hangul, param_string)
\t\tvalue = wr.romanize_one(system_name)
\t\tself.assertEqual(value, expected)''', file=f)

