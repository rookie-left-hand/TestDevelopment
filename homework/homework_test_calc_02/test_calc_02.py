# 补全测试用例加减乘除
# 使用 fixture 装置完成计算器实例的初始化
# 改造 pytest 的运行规则 ,测试用例命名以 calc_开始，加， 减 ，乘，除分别为 calc_add, calc_sub，…
# 自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
# 封装 add, div 测试步骤到 yaml 文件中
import os

import pytest
import yaml

class TestCalc:

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open(
        os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_add_data.yaml'))))
    def calc_add(self, a, b, c, calc):
        print(f"测试数据分别是：{a},{b}")
        result = calc.add(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open(
        os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_add_data.yaml'))))
    def calc_div(self, a, b, c, calc):
        print(f"测试数据分别是：{a},{b}")
        result = calc.add(a, b)
        print(result)
        assert c == result
