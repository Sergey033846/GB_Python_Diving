 # Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
 # Программа должна возвращать сумму и произведение дробей.
 # Для проверки своего кода используйте модуль fractions.
#
# На входе:
# frac1 = "1/2"
# frac2 = "1/3"
#
# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

import fractions

frac1 = '1/2'
frac2 = '1/3'

list1 = frac1.split('/')
list2 = frac2.split('/')

# сокращение дробей по условию не требуется
s = f'{int(list1[0]) * int(list2[1]) + int(list2[0]) * int(list1[1])}/{int(list1[1]) * int(list2[1])}'
p = f'{int(list1[0]) * int(list2[0])}/{int(list1[1]) * int(list2[1])}'

print(f'Сумма дробей: {s}')
print(f'Произведение дробей: {p}')
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}')
print(f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')

# решение автотеста
from fractions import Fraction
#frac1 = '2/5'
#frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
# numerator1_str, denominator1_str = frac1.split('/')
# numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
# numerator1 = int(numerator1_str)
# denominator1 = int(denominator1_str)
# numerator2 = int(numerator2_str)
# denominator2 = int(denominator2_str)
#
# common_denominator = denominator1 * denominator2
#
# new_numerator1 = numerator1 * denominator2
# new_numerator2 = numerator2 * denominator1
#
# summation_numerator = new_numerator1 + new_numerator2
# multiplication_numerator = numerator1 * numerator2
#
# print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
# print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")
#
# # Преобразуем введенные строки в объекты Fraction
# fraction1 = Fraction(frac1)
# fraction2 = Fraction(frac2)
#
# # Вычисляем сумму и произведение дробей
# summation = fraction1 + fraction2
# multiplication = fraction1 * fraction2
#
# print(f"Сумма дробей: {summation}")
# print(f"Произведение дробей: {multiplication}")
