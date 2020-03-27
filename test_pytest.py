import pytest
from pyth.calc import Calc
import yaml
class TestCalc:
    def setup(self):
        self.calc = Calc ( )

    @pytest.mark.parametrize ("a,b,re", yaml.safe_load(open("./adddata.yaml")))
    def test_add(self,a,b,re):
        add = self.calc.add (a,b)
        print(add)
        assert add == re

    @pytest.mark.parametrize ("a,b,re", yaml.safe_load(open("./divdata.yaml")))
    def test_div(self,a,b,re):
        div = self.calc.div (a, b)
        assert div == re
