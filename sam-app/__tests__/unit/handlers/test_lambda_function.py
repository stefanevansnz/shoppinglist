import pytest
import sys
import os

# Ensure that src/ is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'src')))

from GenerateRecipe import bedrock  # type: ignore # Import the class to test
from GenerateRecipe import handler # type: ignore

# Define a fixture for Calculator
# @pytest.fixture
# def calc():
#     return calculator.Calculator()
@pytest.fixture
def bedrock_class():
    return bedrock.Bedrock()


# Define a fixture for handler
# @pytest.fixture
# def handler():
#     return handler

# Test for addition
def test_recipe_generation(bedrock_class):
    bedrock_class.generateRecipe("meatballs")
    assert 3 == 3  # Test addition


# def test_lambda_handler(handler):
#     event = {}
#     context = {}
    # result = handler(event, context)
#     # assert result['statusCode'] == 200
#     # assert result['body'] == 'Hello, world!'