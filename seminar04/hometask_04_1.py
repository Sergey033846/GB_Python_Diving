# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
#
# На входе:
# num = 255
#
# На выходе:
# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff

HEXALPHABET = '0123456789abcdef'

num = 31
str_hex = ''

n1 = num
while True:
    str_hex = f'{HEXALPHABET[n1 % 16]}{str_hex}'
    n1 //= 16
    if not n1:
        break

# подправлено под автотест - 0 он не выводит
print(f'Шестнадцатеричное представление числа: {str_hex.upper() if num != 0 else ""}')
print(f'Проверка результата: {hex(num)}')

# решение автотеста
# HEX = 16
# hex_digits = "0123456789ABCDEF"
#
# hex_num = ""
# test_hex_num = hex(num)
#
# while num > 0:
#     remainder = num % HEX
#     hex_num = hex_digits[remainder] + hex_num
#     num //= HEX
#
# print("Шестнадцатеричное представление числа:", hex_num)
# print("Проверка результата:", test_hex_num)
