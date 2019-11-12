import random
import modules.sfunction

def victory_run(quantity_of_questions = 2):
    s_answers = [
        "07.09.1952",
        "09.09.1941",
        "28.12.1969",
        "16.03.1953",
        "11.08.1950",
        "24.03.1956",
        "28.10.1955",
        "23.06.1912",
        "21.08.1973",
        "11.06.1950"]

    s_questions = [
        "Владимира Путина",
        "Дэнниса Ритчи",
        "Линуса Торвальдса",
        "Ричарда Столлмана",
        "Стива Возняка",
        "Стива Балмера",
        "Билла Гейтса",
        "Алана Тьюринга",
        "Сергея Брина",
        "Бьерна Страуструпа"]

    print('Викторина - "Угадай год рождения знаменитости, будет задано %s вопроса/ов\n' %(quantity_of_questions))

    again = 'да'
    while again == 'да' or again == 'yes':
        correct = 0
        notcorrect = 0

        #выбираем вопросы рандомом
        questions = random.sample(s_questions, quantity_of_questions)

        #получаем индексы вопросов
        i_q = []
        for i in questions:
            i_q.append(s_questions.index(i))

        #по индексам вопросов отбираем соответствующие ответы
        answers = []
        for i in i_q:
            answers.append(s_answers[i])

        #print('====Верные ответы для отладки====')
        #print(questions)
        #print(answers)
        #print('=================================\n')

        print('===Начинаем===')
        for name in range(len(questions)):
            print('Введите дату рождения',questions[name],'в формате dd.mm.yyyy')
            answer = input()
            if answer in answers and answer == answers[name]:
                correct += 1
            else:
                notcorrect += 1
                print(modules.sharedfunc.get_date(answers[name]))

        percent_correct = correct * 100 / len(questions)
        percent_notcorrect = notcorrect * 100 / len(questions)
        print('Подведем итог: ')
        print("Количество правильных ответов: %s " %(correct))
        print("Количество ошибок: %s " %(notcorrect))
        print("Процент правильных ответов: %s " %(percent_correct))
        print("Процент неправильных ответов: %s " %(percent_notcorrect))

        while True:
            again = ''
            if again != 'да' or again != 'yes' or again != 'нет' or again != 'no':
                again = input('Сыграем еще раз? [да(yes)/нет(no)]: \n')
                if again == 'да' or again == 'yes':
                    print('\n===Попробуем еще раз===')
                    break
                elif again == 'нет' or again == 'no':
                    print('===До скорой встречи===')
                    break
                else:
                    print('Некорректный ответ, повторите ввод \n')
        if again == 'да' or again == 'yes':
            continue
        else:
            break