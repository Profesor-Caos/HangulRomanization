from src.database_connector import DatabaseConnector
from typing import Iterable

class KoArticle:
    page_id: int = -1
    page_title: str = ''
    page_text: str = ''
    pronunciation: str = ''

    def __init__(self, page_id, page_title, page_text, pronunciation):
        self.page_id = page_id
        self.page_title = page_title
        self.page_text = page_text
        self.pronunciation = pronunciation

    def write_to_database(self):
        try:
            self.db_connector = DatabaseConnector()
            self.db_connector.connect()
            insert_sql = '''INSERT INTO ko_article (page_id, page_title, page_text, pronunciation) VALUES (%s, %s, %s, %s) as new
                            ON DUPLICATE KEY UPDATE
                            page_title = new.page_title, page_text = new.page_text, pronunciation = new.pronunciation'''
            data = (self.page_id, self.page_title, self.page_text, self.pronunciation)
            self.db_connector.execute_query(insert_sql, data)
        finally:
            self.db_connector.disconnect()

class KoArticles:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.collection = []
        self.index = 0
    
    def __iter__(self) -> 'KoArticles':
        return self
    
    def __next__(self) -> KoArticle:
        if (self.index < len(self.collection)):
            val = self.collection[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    def load_all(self, query = ''):
        try:
            self.db_connector.connect()
            if query == '': query = "SELECT * FROM ko_article"
            results = self.db_connector.execute_query(query)
            self.db_connector.disconnect()
            for result in results:
                self.collection.append(KoArticle(result["page_id"], result["page_title"], result["page_text"], result["pronunciation"]))
        finally:
            self.db_connector.disconnect()
