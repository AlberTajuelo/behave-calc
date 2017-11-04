# Import needed packages
from behave import *
from calc import *

# Step bindings definitions

@given('a calc')
def step_impl(context):
  context.calc = Calculator()

@when('sum {first_number:d} and {second_number:d}')
def step_impl(context, first_number, second_number):
  context.calc.sum_two_numbers(first_number, second_number)

@then('the result is {result:d}')
def step_impl(context, result):
  assert context.calc.last_result == result