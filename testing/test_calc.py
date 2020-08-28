#!-*- coding:utf-8 -*-
import pytest
from pythoncode.calc import Calc
from utils import utils


class TestCalc:
    path = './testdata/calc_datas'
    data = utils.yamlload(path)

    def setup_class(self):
        self.cal = Calc()
        print("start test:")

    def teardown_class(self):
        print("test finished.")

    @pytest.mark.parametrize('a, b, ans', data)
    def test_add(self, a, b, ans):
        c = self.cal.add(a, b)
        assert ans == c

    def test_minus(self, a, b, ans):
        c = self.cal.minus(a, b)
        assert ans == c


