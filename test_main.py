from main import check_number, look_for_John, is_it_array
import pytest

# Check_number tests

def test_check_number_greater_than_7():
    assert check_number("9") == "Hello"

def test_check_number_less_than_7():
    assert check_number("6") == "Number is lower than 7 or equal to 7"