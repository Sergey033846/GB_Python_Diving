# 2 - Задача о 8 ферзях
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя функцию is_attacking(q1,q2), 
# проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

# Пример использования.
# На входе:
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 
# На выходе:
# False

# 3 - Расстановка ферзей
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого. 
# Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
# Пример использования 
# На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]


import random as rnd


__all__ = ['print_chessboard', 'generate_boards']


# печать линии псевдографики
def print_chessboard_border_line(left_char, main_char, separator_char, right_char):    
    print(f'  {left_char}', *(separator_char * 7), right_char, sep=main_char * 4)


# печать строки с обозначениями (first_column_label = '1' или 'a')
def print_chessboard_columns_labels(first_column_label):    
    print(' ', *(f'{chr(ord(first_column_label) + col):>4}' for col in range(8)))


# вывод шахматной доски на экран терминала с указанием положений 8 ферзей
def print_chessboard(queens_positions):
    # печать верхней строки с обозначениями
    print_chessboard_columns_labels('1')

    # выводим верх доски
    print_chessboard_border_line('┌', '─', '┬', '┐')

    # выводим ряды
    for row in range(8):
        # клетки и их содержимое
        print(f'{8 - row} ', '│', sep='', end='')    
        for col in range(8):        
            if (8 - row, col + 1) in queens_positions:
                position_id = queens_positions.index((8 - row, col + 1))
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 and col % 2):    # если ферзь стоит на "белой" клетке, печатаем черным на зеленом, иначе, зеленым на черном
                    print(f' \033[42m\033[30m{f'Ф{position_id + 1}'}\033[0m ', '│', sep='', end='')
                else:
                    print(f' \033[40m\033[32m{f'Ф{position_id + 1}'}\033[0m ', '│', sep='', end='')
            else:                    
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 and col % 2):
                    print(f' \033[37m{'█' * 2}\033[0m ', '│', sep='', end='')    # пустые "белые" клетки
                else:
                    print(f' {'  '} ', '│', sep='', end='')                      # пустые "черные" клетки
        print(f' {8 - row}')       
        # разделитель рядов
        if row < 7:        
            print_chessboard_border_line('├', '─', '┼', '┤')

    # выводим низ доски
    print_chessboard_border_line('└', '─', '┴', '┘')    

    # печать нижней строки с обозначениями
    print_chessboard_columns_labels('1')


# проверка, бьют ли ферзи друг друга
def is_attacking(q1, q2):    
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


# проверка всех возможных пар ферзей
def check_queens(*, queens):
    for iq1 in range(len(queens) - 1):
        for q2 in queens[iq1 + 1:]:
            if is_attacking(queens[iq1], q2):
                return False
    return True


# генерация четырех успешных расстановок 8 ферзей
def generate_boards() -> list:
    queens_count = 8
    placement_count = 4        
    result = []
    max_iteration_limit = 64

    while (len(result) < placement_count):
        placement = []
        
        for _ in range(queens_count):
            
            iteration_count = 0            
            while iteration_count < max_iteration_limit:
                f = (rnd.randint(1, 8), rnd.randint(1, 8))
                placement.append(f)
                if check_queens(queens=placement):
                    break
                else:
                    placement.remove(f)
                    iteration_count += 1
            else:                
                break      
        
        if len(placement) == queens_count:
            placement.sort()
            if not placement in result:
                result.append(placement)

    return result


if __name__ == '__main__':        
    # задача 2
    queens_ = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]     
    print(check_queens(queens=queens_))
    # print_chessboard(queens)

    # задача 3
    board_list = generate_boards()
    print(board_list)
    # print(board_list[0], check_queens(queens=board_list[0]))
    # print(board_list[1], check_queens(queens=board_list[1]))
    # print(board_list[2], check_queens(queens=board_list[2]))
    # print(board_list[3], check_queens(queens=board_list[3]))
    # print_chessboard(board_list[0])
    # print_chessboard(board_list[1])
    # print_chessboard(board_list[2])
    # print_chessboard(board_list[3])


# решение автотеста (задача 2)
# from itertools import combinations

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True


# решение автотеста (задача 3)
# import random
# from itertools import combinations

# def generate_board():
#     # Генерируем случайную доску
#     board = []

#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list
