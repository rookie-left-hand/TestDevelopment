import pytest
from python_code.calc import Calc

print()
@pytest.fixture()
def calc():
    calc = Calc()
    return calc

def pytest_configure(config):
    marker_list = ["add", "sub", "mul", "div"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )

def pytest_collection_modifuitems(session,config,items:list):
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif "mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)