# @Time:2020/5/8 13:49
# @Author:luanfusheng
# @File:test_calc.py
# @Software:PyCharm
import yaml

from python_code.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./test_add_data.yaml")))
    def test_add(self,a,b,c):
        print(f"测试数据分别是：{a},{b}")
        print(yaml.safe_load(open("./test_add_data.yaml")))
        result = self.calc.add(a,b)
        print(result)
        assert c == result

if __name__ == '__main__':
    pytest.main(['-v','test_calc.py'])