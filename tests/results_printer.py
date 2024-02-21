import io
import inspect
from test_unique_db_cases import TestUniqueDBCases
from test_all_wiki_articles import TestAllWikiArticles

with open("tests/test_unique_db_cases_results.txt", "w", encoding="utf-8") as f:
    tudc = TestUniqueDBCases()
    tudc.set_file(f)
    for method_name in dir(tudc):
        method_attr = getattr(tudc, method_name)
        if inspect.ismethod(method_attr) and method_attr.__func__ in TestUniqueDBCases.__dict__.values():
            signature = inspect.signature(method_attr)
            if (len(signature.parameters) == 0):
                getattr(tudc, method_name)()

with open("tests/test_all_wiki_articles_results.txt", "w", encoding="utf-8") as f:
    tawa = TestAllWikiArticles()
    tawa.set_file(f)
    for method_name in dir(tawa):
        method_attr = getattr(tawa, method_name)
        if inspect.ismethod(method_attr) and method_attr.__func__ in TestAllWikiArticles.__dict__.values():
            signature = inspect.signature(method_attr)
            if (len(signature.parameters) == 0):
                getattr(tawa, method_name)()