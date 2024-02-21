import json
from src.models.ko_article import KoArticles
from src.wiktionary_romanization import WiktionaryRomanization

articles = KoArticles()
articles.load_all("select * from ko_article where romanization != ''")
with open("tests/test_all_wiki_articles.py", "w", encoding="utf-8") as f:
    print('''import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestAllWikiArticles(unittest.TestCase):
\tfile = ''

\tdef set_file(self, file):
\t\tself.file = file
''', file=f)
    for article in articles:
        romanization_jsons = article.romanization.split(';;;')
        for i, romanization_json in enumerate(romanization_jsons):
            romanization = json.loads(romanization_json)
            for name in ["ph", "rr", "rrr", "mr", "yr", "ipa"]:
                wr = WiktionaryRomanization(article.page_title, romanization["pronunciation"])
                try:
                    value = wr.romanize_one(name)
                    if value != romanization[name]:
                        print(f'''\tdef test_{romanization["rr"].replace(' ', '_').replace("'", "").replace("/", "_").replace("(", "").replace(")", "")}_{name}{"_" + str(i) if i > 0 else ''}(self):\n\t\treturn self.run_test("{article.page_title}", "{romanization["pronunciation"]}", "{romanization[name]}", "{name}")''', file=f)
                except Exception as e:
                    print(f'''\tdef test_{romanization["rr"].replace(' ', '_').replace("'", "").replace("/", "_").replace("(", "").replace(")", "")}_{name}{"_" + str(i) if i > 0 else ''}(self):\n\t\treturn self.run_test("{article.page_title}", "{romanization["pronunciation"]}", "{romanization[name]}", "{name}")''', file=f)
    print('''
\tdef run_test(self, hangul, param_string, expected, system_name):
\t\twr = WiktionaryRomanization(hangul, param_string)
\t\tif (self.file):
\t\t\ttry:
\t\t\t\tvalue = wr.romanize_one(system_name)
\t\t\t\tprint(f"{inspect.stack()[1].frame.f_code.co_name}: { 'success' if value == expected else f'fail expected {expected} but received {value}'}", file=self.file)
\t\t\t\treturn value == expected
\t\t\texcept Exception as e:
\t\t\t\tprint(f"{inspect.stack()[1].frame.f_code.co_name}: fail {e}", file=self.file)
\t\t\t\treturn False
\t\telse:
\t\t\tvalue = wr.romanize_one(system_name)
\t\t\tself.assertEqual(value, expected)''', file=f)
