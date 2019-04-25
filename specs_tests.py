# Writing our tests first
# Your calculator should
    #Add, Subtract, Multiply and Divide
# Random list of tests
# Tests for data type
# Tests for addition method
# Tests for subtraction method
# Tests for multiplication method
# Tests for division method
# Test if last result was recorded

from calculator import *
# Tests have 2 minimum sections
# Setup
# Assertion (To check what is true or false)

calculator_instance = Calculator()
# Testing addition
print('Testing addition')
print(calculator_instance.add(10, 10)==20)
print(calculator_instance.add(100, 1)==101)
print(type(calculator_instance.add(1, 1))== int)
# Testing subtraction
print('Testing subtraction')
print(calculator_instance.subtract(10, 10)==0)
print(calculator_instance.subtract(100, 1)==99)
print(type(calculator_instance.subtract(1, 1))== int)
# Testing division
print('Testing division')
print(calculator_instance.divide(10, 10)==1)
print(calculator_instance.divide(100, 1)==100)
print(type(calculator_instance.divide(1, 1))== float or int)
# Testing multiplication
print('Testing multiplication')
print(calculator_instance.multiply(10, 10)==100)
print(calculator_instance.multiply(100, 1)==100)
print(type(calculator_instance.multiply(1, 1))== int)
# Testing last result was recorded
print('Testing last result')
calculator_instance.multiply(100, 1)==100
print(calculator_instance.last_result == 100)