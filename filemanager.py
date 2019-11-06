import modules.function as fm
import two_apps.bankaccount as ba
import two_apps.victory as vg

while True:
    print('-----------------------------------------')
    print('            Файловый менеджер            ')
    print('-----------------------------------------')
    print(' 1 - Создать папку')
    print(' 2 - Удалить (файл/папку)')
    print(' 3 - Копировать (файл/папку)')
    print(' 4 - Просмотр содержимого рабочей директории')
    print(' 5 - Посмотреть только папки')
    print(' 6 - Посмотреть только файлы')
    print(' 7 - Просмотр информации об операционной системе')
    print(' 8 - Создатель программы')
    print(' 9 - Играть в викторину')
    print(' 10 - Мой банковский счет')
    print(' 0 - Выход')

    choice = input('\nВыберете пункт меню и введите с клавиатуры его номер\n')
    if choice == '1':
        fm.dir_create()
    elif choice == '2':
        fm.dir_file_remove()
    elif choice == '3':
        fm.dir_file_copy()
    elif choice == '4':
        fm.list_files_and_dirs()
    elif choice == '5':
        fm.list_dirs()
    elif choice == '6':
        fm.list_files()
    elif choice == '7':
        fm.watch_os_info()
    elif choice == '8':
        fm.about_creator()
    elif choice == '9':
        quantity_of_questions = 0
        while quantity_of_questions > 10 or quantity_of_questions < 2:
            print('Введите количество вопросов от 2 до 10\n')
            quantity_of_questions = int(input())
        vg.victory_run(quantity_of_questions)
    elif choice == '10':
        ba.balance_run()
    elif choice == '0':
        break
    else:
        print('Неверный пункт меню')
