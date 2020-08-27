#! /user/bin/env python
# encoding: utf-8


# 实现简单的计算器功能
class Calculator:
    def add(self, a, b):
        c = a + b
        print("result is:", c)
        return c

    def minus(self, a, b):
        c = a - b
        return c

    def multiply(self, a, b):
        c = a * b
        return c

    def div(self, a, b):
        c = a / b
        return c
