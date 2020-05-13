#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type hints 类型提示
class Calc:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


print(Calc().mul(600000,6000000))