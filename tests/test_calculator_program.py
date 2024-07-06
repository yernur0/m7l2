import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_subtraction():
    assert calculate(5, 1, '-') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_division_by_zero():
    assert calculate(10, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_float_division():
    assert calculate(5, 2, '/') == 2.5

def test_calculate_negative_numbers():
    assert calculate(-5, 3, '+') == -2

def test_calculate_large_numbers():
    assert calculate(1000000, 2000000, '-') == -1000000

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
