import os

import pytest
import yaml

from python_code.calc import Calc


@pytest.fixture()
def calc():
    calc = Calc()
    return calc


@pytest.fixture(autouse=True)
def steps():
    """
    获取测试步骤
    :return: steps
    """
    steps = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_steps.yaml')))
    return steps

def pytest_collection_modifyitems(session,config,items:list):
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif "mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)