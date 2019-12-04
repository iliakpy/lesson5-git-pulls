"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import pickle
import modules.sfunction

FILE_BALANCE = 'total_balance.log'
FILE_HISTORY = 'purchase_history.log'

def money_in(balance):
    print('Введите сумму пополнения в рублях\n')
    money_input = modules.sfunction.check_input()
    balance += money_input
    print('Зачислено! Ваш баланс: %s' % balance)
    return balance


def purchase(l_balance, l_history):
    print('Введите сумму покупки:\n')
    purchase_input = modules.sfunction.check_input()
    if purchase_input > l_balance:
        print('Недостаточно средств на счету')
        input('Нажмите ввод для возвращения в главное меню')
    else:
        l_balance -= purchase_input
        print('Введите название покупки')
        purchase_item = input()
        l_history[purchase_item] = purchase_input
    return l_balance, l_history


def show_history(history):
    print('История покупок:')
    for k, v in history.items():
        print('Куплено %s ---- за %s руб.\n' % (k, v))
    input('Нажмите ввод для возвращения в главное меню')

def save_balance_file(balance):
    balance_to_write = str(balance)
    with open(FILE_BALANCE, 'w') as f:
        f.write(balance_to_write)


def save_history_file(history):
    with open(FILE_HISTORY, "wb") as f:
        pickle.dump(history, f)

def balance_run():
    if not os.path.exists(FILE_BALANCE):
        balance = 0.00
    else:
        with open(FILE_BALANCE, 'r') as f:
            strbalance = f.read()
            balance = float(strbalance)
    if not os.path.exists(FILE_HISTORY):
        history = {}
    else:
        with open(FILE_HISTORY, 'rb') as f:
            history = pickle.load(f)

    while True:
        print('Ваш текущий баланс:%s\n' % balance)
        print('=== Главное меню ===')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('\nВыберите операцию\n')
        if choice == '1':
            balance = money_in(balance)
        elif choice == '2':
            balance, history = purchase(balance, history)
        elif choice == '3':
            show_history(history)
        elif choice == '4':
            save_balance_file(balance)
            save_history_file(history)
            break
        else:
            print('Неверный пункт меню')