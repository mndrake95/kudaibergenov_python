from main import check_number, look_for_John, is_it_array
import pytest

# Check_number tests

@pytest.mark.parametrize("input_val, expected", [
    ("9", "Hello"),
    ("7.5", "Hello"),
    ("100", "Hello")
])

def test_check_number_greater_than_7(input_val, expected):
    assert check_number(input_val) == expected

@pytest.mark.parametrize("input_val", [
    ("7"),
    ("6"),
    ("-1"),
    ("0")
])

def test_check_number_less_than_7_or_equal(input_val):
    assert "is lower" in check_number(input_val) 

@pytest.mark.parametrize("input_val", [
    ("abc"),
    ("John")
])

def test_check_number_invalid_input(input_val):
    assert "Caught an error" in check_number(input_val)


# Look_for_John tests

@pytest.mark.parametrize("input_val, expected", [
    ("John", "Hello, John")
])

def test_look_for_John_John_is_here(input_val, expected):
    assert look_for_John(input_val) == expected

@pytest.mark.parametrize("input_val", [
    ("john"), 
    ("Sam"),
    ("Alice")
])

def test_look_for_John_other_name(input_val):
    assert "no such name" in look_for_John(input_val)

@pytest.mark.parametrize("input_val", [
    ("5"),
    ("7.5"),
    ("-1")
])

def test_look_for_John_number(input_val):
    assert "is number" in look_for_John(input_val)

@pytest.mark.parametrize("input_val", [
     ("1,2,3"),
     ("1;2;3"), 
     ("1 2 3")
])

def test_look_for_John_array(input_val):
    assert "is array" in look_for_John(input_val)

# Is_it_array tests

@pytest.mark.parametrize("input_val, expected", [
    ("3,6,9", "3 6 9"),
    ("3;6;9", "3 6 9"),
    ("3 6 9", "3 6 9")
])

def test_is_it_array_valid_array_correct_sep(input_val, expected):
    assert is_it_array(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    ("1,2,4", "Array is empty"),
    ("1;2;4", "Array is empty"),
    ("1 2 4", "Array is empty")
])

def test_is_it_array_no_multiples_correct_sep(input_val, expected):
    assert is_it_array(input_val) == expected

@pytest.mark.parametrize("input_val", [
    ("John"),
    ("abc,def")
])

def test_is_it_array_invalid_input(input_val):
    assert "Caught an error" in is_it_array(input_val)

@pytest.mark.parametrize("input_val, expected", [
    ("1,2,3,4,5,6", "3 6"),
    ("1;3;5;9", "3 9")
])

def test_is_it_array_mixed_arrays(input_val, expected):
    assert is_it_array(input_val) == expected