# 补全测试用例加减乘除
# 使用 fixture 装置完成计算器实例的初始化
# 改造 pytest 的运行规则 ,测试用例命名以 calc_开始，加， 减 ，乘，除分别为 calc_add, calc_sub，…
# 自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
# 封装 add, div 测试步骤到 yaml 文件中
import os

import pytest
import yaml


def get_data(key):
    """
    根据key值获取测试数据
    :return: vaules
    """
    test_data = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_data.yaml')))
    return test_data[key]


class TestCalc:

    # @pytest.mark.parametrize(["a", "b", "c"], get_data('add'))
    # def calc_add(self, a, b, c, calc):
    #     print(f"测试数据分别是：{a},{b}")
    #     result = calc.add(a, b)
    #     print(result)
    #     assert c == result
    #
    # @pytest.mark.parametrize(["a", "b", "c"], get_data('div'))
    # def calc_div(self, a, b, c, calc):
    #     print(f"测试数据分别是：{a},{b}")
    #     result = calc.add(a, b)
    #     print(result)
    #     assert c == result
    #
    # @pytest.mark.parametrize(["a", "b", "c"], get_data('sub'))
    # def test_sub(self, a, b, c, calc):
    #     print(f"测试数据分别是：{a},{b}")
    #     result = calc.add(a, b)
    #     print(result)
    #     assert c == result
    #
    # @pytest.mark.parametrize(["a", "b", "c"], get_data('mul'))
    # def calc_mul(self, a, b, c, calc):
    #     print(f"测试数据分别是：{a},{b}")
    #     result = calc.add(a, b)
    #     print(result)
    #     assert c == result

    @pytest.mark.parametrize(("a", "b", "expect"), get_data("mul"))
    def calc_mul(self, a, b, expect, calc):
        result = calc.mul(a, b)
        assert expect == result

if __name__ == '__main__':
    pytest.main()