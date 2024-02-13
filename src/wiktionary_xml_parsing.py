from bigxml import Parser, xml_handle_element, xml_handle_text
from dataclasses import dataclass
from controllers.ko_article_controller import KoArticleController
import re

hangul_regex = re.compile(r'[\u1100-\u11FF\u3130-\u318F\uA960-\uA97F\uAC00-\uD7AF\uD7B0-\uD7FF]+')

@xml_handle_element("mediawiki", "page")
@dataclass
class Page:
    title: str = 'N/A'
    text: str = 'N/A'
    id: int = -1

    @xml_handle_element("id")
    def handle_id(self, node):
        self.id = int(node.text)

    @xml_handle_element("title")
    def handle_title(self, node):
        self.title = node.text

    @xml_handle_element("revision", "text")
    def handle_text(self, node):
        self.text = node.text

ko_article_controller = KoArticleController()

# Step 1 writing all the korean articles to the database
# with open("data\enwiktionary-20240120-pages-articles.xml", 'rb') as f:
#     for item in Parser(f).iter_from(Page):
#         #print(item.title)
#         if (hangul_regex.search(item.title)):
#             # print(item.title)
#             # print(item.text)
#             ko_article_controller.create_article(item.id, item.title, item.text)

# Step 2, added another column for what's important in the pronunciation section and
# writing that to the DB
ko_article_controller.update_pronunciation()
            
