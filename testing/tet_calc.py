#! /user/bin/env python
# encoding: utf-8
"""
计算器的测试用例
"""
import pytest

from pythoncode.calc import Calculator


class TestCalc:
    cal = Calculator()

    def setup(self):
        print("start to test:")

    def teardown(self):
        print("test finished!\n")

    @pytest.mark.parametrize('a, b, expect_result', [
        [1, 1, 2],
        [1000000, 1000000, 2000000],
        [0.1, 0.2, 0.3],
        [-1, -2, -3],
        ['a', 'b', 'ab'],
        [None, 1, 1],
        [False, True, True],
        [False, False, False]
    ])
    def test_add(self, a, b, expect_result):
        result = self.cal.add(a, b)
        assert expect_result == result

    def test_minus(self, a, b, expect_result):
        result = self.cal.minus(a, b)
        assert expect_result == result
