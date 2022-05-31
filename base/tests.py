# Create your tests here.
from base.tasks import somar


class TestBase:
    def test_base(self):
        assert somar(1, 2) == 3
