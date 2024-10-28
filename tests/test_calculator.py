import pytest
from calculator import RPNCalculator

@pytest.fixture
def calculator():
    calc = RPNCalculator()
    calc.create_stack("test_stack")
    return calc

def test_push_and_pop(calculator):
    calculator.push("test_stack", 5)
    assert calculator.pop("test_stack") == 5

def test_clear(calculator):
    calculator.push("test_stack", 1)
    calculator.push("test_stack", 2)
    calculator.clear("test_stack")
    assert calculator.get_stack("test_stack") == []

def test_addition(calculator):
    calculator.push("test_stack", 3)
    calculator.push("test_stack", 4)
    calculator.operate("test_stack", '+')
    assert calculator.pop("test_stack") == 7

def test_subtraction(calculator):
    calculator.push("test_stack", 10)
    calculator.push("test_stack", 4)
    calculator.operate("test_stack", '-')
    assert calculator.pop("test_stack") == 6

def test_multiplication(calculator):
    calculator.push("test_stack", 3)
    calculator.push("test_stack", 4)
    calculator.operate("test_stack", '*')
    assert calculator.pop("test_stack") == 12

def test_division(calculator):
    calculator.push("test_stack", 12)
    calculator.push("test_stack", 3)
    calculator.operate("test_stack", '/')
    assert calculator.pop("test_stack") == 4

def test_division_by_zero(calculator):
    calculator.push("test_stack", 5)
    calculator.push("test_stack", 0)
    with pytest.raises(ValueError, match="Division by zero"):
        calculator.operate("test_stack", '/')

def test_insufficient_operands(calculator):
    calculator.push("test_stack", 5)
    with pytest.raises(ValueError, match="Not enough operands"):
        calculator.operate("test_stack", '+')

def test_unknown_operator(calculator):
    calculator.push("test_stack", 5)
    calculator.push("test_stack", 3)
    with pytest.raises(ValueError, match="Unknown operator"):
        calculator.operate("test_stack", '%')