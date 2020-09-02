#!-*- coding:utf-8 -*-
import pytest
from pythoncode.calc import Calc
from utils import utils


class TestCalc:
    path_add = './testdata/calc_datas'
    path_mul = './testdata/mul_data'
    data_add = utils.yamlload(path_add)
    data_mul = utils.yamlload(path_mul)


    def setup_class(self):
        self.cal = Calc()
        print("start test:")

    def teardown_class(self):
        print("test finished.")

    @pytest.mark.parametrize('a, b, ans', data_add)
    def test_add(self, a, b, ans):
        c = self.cal.add(a, b)
        assert ans == c

    @pytest.mark.parametrize('a, b, ans', data_add)
    def test_minus(self, a, b, ans):
        c = self.cal.minus(ans, b)
        assert a == c

    @pytest.mark.parametrize('a, b, ans', data_mul)
    def test_multi(self, a, b, ans):
        c = self.cal.mul(a, b)
        assert ans == c

    @pytest.mark.parametrize('a, b, ans', data_mul)
    def test_div(self, a, b, ans):
        c = self.cal.div(ans, b)
        assert a == c


