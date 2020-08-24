#!-*- coding:utf-8 -*-
import pytest

from pythoncode.calc import Calc


class TestCalc:
    def setup_class(self):
        self.cal = Calc()
        print("start test:")

    def teardown_class(self):
        print("test finished.")

    @pytest.mark.parametrize('a, b, ans', [
        (1, 1, 2),
        (0.5, 0.6, 1.1),
        (100000, 100000, 200000),
        (-1, -2, -3),
        ('a', 'b', 'ab')
    ])
    def test_add(self, a, b, ans):
        c = self.cal.add(a, b)
        assert ans == c
