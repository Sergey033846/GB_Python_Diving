# Задание №3
# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# - Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# - Избегайте магических чисел
# - Добавьте аннотацию типов где это возможно

BASIS_OF_THE_NUMBER_SYSTEM_BIN = 2
BASIS_OF_THE_NUMBER_SYSTEM_OCT = 8

n: int = 255
str_bin: str = ''
str_oct: str = ''

n1 = n

# не стал делать условие через 'while n1' для случая, если n == 0
while True:
    str_bin = f'{n1 % BASIS_OF_THE_NUMBER_SYSTEM_BIN}{str_bin}'
    n1 //= BASIS_OF_THE_NUMBER_SYSTEM_BIN
    if not n1:
        break

n1 = n
while True:
    str_oct = f'{n1 % BASIS_OF_THE_NUMBER_SYSTEM_OCT}{str_oct}'
    n1 //= BASIS_OF_THE_NUMBER_SYSTEM_OCT
    if not n1:
        break

print(n)
print(f'0b{str_bin} {bin(n)}')
print(f'0o{str_oct} {oct(n)}')


