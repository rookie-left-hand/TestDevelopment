import pytest
from python_code.calc import Calc


@pytest.fixture()
def calc():
    calc = Calc()
    return calc