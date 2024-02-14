from src.models.ko_article import KoArticle, KoArticles
import re

class KoArticleController:
    def __init__(self):
        self.model = KoArticle
        return
    
    def create_article(self, page_id, page_title, page_text):
        article = KoArticle(page_id, page_title, page_text)
        article.write_to_database()

    def load_all_articles(self):
        articles = KoArticles()
        articles.load_all()
        return articles

    def update_pronunciation(self):
        articles = self.load_all_articles()
        for article in articles:
            pronunciation = article.pronunciation
            text = article.page_text
            pattern = r'(\{\{ko-ipa.*\}\})(?![\s\S]*\1)'
            # matches {{ko-ipa}} with anything between ipa and the closing }}, then looks ahead to make sure it doesn't appear again
            # with a negative lookahead. This captures the last instance in the text of each distinct use of ko-ipa.
            matches = re.findall(pattern, text, re.IGNORECASE)
            new_pronunciation = ', '.join(matches)
            if (new_pronunciation == pronunciation):
                continue
            if (pronunciation != '' and new_pronunciation != pronunciation):
                print(f"Updated pronunciation: {article.page_title} from {pronunciation} to {new_pronunciation}")
            article.pronunciation = new_pronunciation
            article.write_to_database()