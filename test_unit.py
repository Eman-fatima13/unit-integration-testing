import pytest
from bank_app import *

def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)

def test_withdraw_valid():
    assert withdraw(1000, 500) == 500

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(500, 1000)

def test_calculate_interest():
    assert calculate_interest(1000, 10, 2) == 1210.0

def test_check_loan_eligibility_true():
    assert check_loan_eligibility(6000, 750) is True

def test_check_loan_eligibility_false():
    assert check_loan_eligibility(2000, 600) is False