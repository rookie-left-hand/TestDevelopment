# @Time:2020/5/8 13:49
# @Author:luanfusheng
# @File:test_calc.py
# @Software:PyCharm
import os
import yaml
from python_code.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open(os.path.dirname(__file__) + "\\test_add_data.yaml")))
    def test_add(self, a, b, c):
        print(f"测试数据分别是：{a},{b}")
        result = self.calc.add(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open(os.path.dirname(__file__) + "\\test_div_data.yaml")))
    def test_div_01(self, a, b, c):
        """正常情况下测试"""
        print(f"测试数据分别是：{a},{b}")
        result = self.calc.div(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(["a", "b"], [(5, 0)])
    def test_div_02(self, a, b):
        """除数为零"""
        print(f"测试数据分别是：{a}, {b}")
        with pytest.raises(ZeroDivisionError):
            self.calc.div(5, 0)
        # print(self.calc.div(5, 0))

    @pytest.mark.parametrize(["a", "b"], [(10, 3)])
    def test_div_03(self, a, b):
        """商为无限循环小数时"""
        print(f"测试数据分别是：{a}, {b}")
        result = self.calc.div(a, b)
        assert 3.333333333 == round(result, 9)


if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])
