from pytest import *
from account import *

class Test:

    def setup_method(self):
        self.account_one = Account('Osmar')

    def teardown_method(self):
        del self.account_one

    def test_init(self):
        assert self.account_one.get_name() == 'Osmar'
        assert self.account_one.get_balance() == 0


    def test_deposit(self):

        assert self.account_one.deposit(20.1) is True
        assert self.account_one.deposit(40.5) is True
        assert self.account_one.deposit(0) is False
        assert self.account_one.deposit(-15) is False
        assert self.account_one.get_balance() == approx(60.6, abs=0.001)



    def test_withdraw(self):

        assert self.account_one.withdraw(20.10) is False
        assert self.account_one.withdraw(40.50) is False
        assert self.account_one.withdraw(-40.50) is False
        assert self.account_one.withdraw(0) is False
        self.account_one.deposit(250)
        assert self.account_one.withdraw(100) is True
        assert (self.account_one.get_balance()) == approx(150, abs=0.001)
