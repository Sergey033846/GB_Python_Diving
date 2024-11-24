# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

# два цикла
# for j in range(1, 21):
#     if j not in [1, 11]:
#         y = j % 10 if j % 10 else 10
#
#         for i in range(2, 6):
#             x = i + 4 if j > 10 else i
#
#             print(f'{x:<3}Х{y:>3} = {x * y:>2}', end='')
#             if i != 5:
#                 print(' ' * 8, end='')
#
#         print()
#
#         if j == 10:
#             print()

# три цикла
for k in (1, 2):
    for y in range(2, 11):
        for i in range(2, 6):
            x = i + 4 if k == 2 else i

            print(f'{x:<3}Х{y:>3} = {x * y:>2}', end='')
            if i != 5:
                print(' ' * 8, end='')
        print()

    print()
