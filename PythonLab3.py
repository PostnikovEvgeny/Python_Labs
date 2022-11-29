#-*- coding: cp1251 -*-
from random import randint
from pyDatalog import pyDatalog
number = 10
pyDatalog.create_terms('X, Y, Result, Sum, Average, Range, RandSum, Median, Rand')

print(f"Сумма элементов ряда 0 - {number}:\n")
(Sum[Range] == sum_(X, for_each = X)) <= X.in_(range_(Range + 1))
print(f"{Sum == Sum[number]}\n")
