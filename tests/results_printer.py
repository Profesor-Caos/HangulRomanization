import io
import inspect
from test_unique_db_cases import TestUniqueDBCases

with open("tests/results.txt", "w", encoding="utf-8") as f:
    tudc = TestUniqueDBCases()
    tudc.set_file(f)
    for method_name in dir(tudc):
        method_attr = getattr(tudc, method_name)
        if inspect.ismethod(method_attr) and method_attr.__func__ in TestUniqueDBCases.__dict__.values():
            signature = inspect.signature(method_attr)
            if (len(signature.parameters) == 0):
                getattr(tudc, method_name)()