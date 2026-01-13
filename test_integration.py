import pytest
from bank_app import *

def test_transfer_success():
    b1, b2 = transfer(2000, 1000, 500)
    assert b1 == 1500
    assert b2 == 1500

def test_transfer_and_interest():
    b1, b2 = transfer(6000, 2000, 1000)
    b2 = calculate_interest(b2, 10, 1)
    assert b2 == 3300.0

def test_transfer_fail():
    with pytest.raises(ValueError):
        transfer(500, 1000, 1000)
