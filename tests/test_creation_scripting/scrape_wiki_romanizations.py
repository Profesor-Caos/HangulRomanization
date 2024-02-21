import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from src.models.ko_article import KoArticles

articles = KoArticles()
articles.load_all("select * from ko_article where pronunciation != '' and romanization = ''")
for article in articles:
    romanizations = []
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
        if not sk_standard_link:
            break # It's possible these can be commented out
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
            romanizations_object = {}
            romanizations_object["pronunciation"] = pronunciation
            for name, expected in zip(["ph", "rr", "rrr", "mr", "yr", "ipa"], [ph_text, rr.text, rrr.text, mr.text, yc.text, ipa_span.text]):
                romanizations_object[name] = expected
            romanizations.append(json.dumps(romanizations_object))
            break
    article.romanization = ";;;".join(romanizations)
    article.write_to_database()

