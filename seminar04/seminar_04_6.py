# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

wallet = 0
operation = None
every_third_count = 0

while operation != 'q':
    operation = input('Введите операцию (+, -, q): ')
    if operation in ['+', '-']:

        amount = 0
        while amount == 0 or amount % 50 != 0:
            amount = int(input('Введите сумму, кратную 50 у.е.: '))

        # вычет налога на богатство
        if wallet > 5000000:
            tax = wallet * 0.10
            wallet -= tax
            print(f'Вычтен налог на богатство {tax:.2f} у.е.')
            print(f'Сумма на счете: {wallet}')

        if operation == '+':
            wallet += amount
            print(f'Пополнение {amount} у.е.')
            print(f'Сумма на счете: {wallet}')
            every_third_count += 1
        elif operation == '-':
            # расчет комиссии за снятие
            fee = amount * 0.015
            if fee < 30:
                fee = 30
            elif fee > 600:
                fee = 600

            if wallet + fee < amount:
                print('Недостаточно средств!')
            else:
                wallet -= amount + fee
                print(f'Снятие {amount} у.е. Комиссия {fee:.2f} у.е.')
                print(f'Сумма на счете: {wallet}')
                every_third_count += 1

        # начисление процентов после каждой третьей операции
        if every_third_count == 3:
            percentages = wallet * 0.03
            wallet += percentages
            print(f'Начислены проценты (после каждой третьей операции): {percentages:.2f}')
            print(f'Сумма на счете: {wallet}')
            every_third_count = 0
    else:
        print(f'Сумма на счете: {wallet}')
        print('Завершение сеанса обслуживания.')


