>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1')  + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>>     

>>> setone = {1, 2, 3}
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3}
{1, 2, 3}
>>> setone | {1, 3, 7}
{1, 2, 3, 7}
>>>


print("use for termainl")