import pytest
import sys
import os

# Ensure that src/ is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'src')))

from GenerateRecipe import calculator  # type: ignore # Import the class to test

# Define a fixture for Calculator
@pytest.fixture
def calc():
    return calculator.Calculator()

# Test for addition
def test_add(calc):
    assert calc.add(1, 2) == 3  # Test addition

# from import lambda_handler

# def test_lambda_handler():
#     event = {}
#     context = {}
#     result = lambda_handler(event, context)
#     assert result['statusCode'] == 200
#     assert result['body'] == 'Hello, world!'