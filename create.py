import model.test

procent_error = 30

def examination_poof(poof, queue_vector):
    try:
        count = 0
        print(queue_vector)
        for vector in queue_vector:
            count = count + 1
            # print(count, poof.get_word())
            # print(poof.get_word(), vector.get_end().get_word())
            list_hex_word = comparison_poof(poof.get_word(), vector.get_end().get_word(), poof) # Вызвать функцию проверки предложения


        # for i in queue_vector:
        #     print(i.get_end().get_word(), poof.get_word())
        #     if i.get_end().get_word() != list_hex_word:
        #         print(1)

        # print('1')
        # print(poof.get_word())
        if (poof.get_word() != list_hex_word):
            print('1')
            vector.get_end().update_data(list_hex_word)
            queue_vector.append(model.vector.Vector(queue_vector[-1].get_end(), vector.get_end()))

        else:
            print('2')
            poof = model.test.Hash_word(" ".join(list_hex_word))  # Строку преобрзовать объект Hash_word
            # print(list_hex_word, poof)
            queue_vector.append(model.vector.Vector(queue_vector[-1].get_end(), poof))

    except UnboundLocalError:
        print("Размер списков отличается")

    except TypeError:
        print("Строки отличатся")
        pass

    # for i in queue_vector:
    #     print(i.get_end().get_word(), poof.get_word())
    #     if i.get_end().get_word() != list_hex_word:
    #         print(1)
    #     # queue_vector.append(model.vector.Vector(queue_vector[-1].get_end(), poof))




def comparison_poof(test, test2, poof) -> list:
    # если количество слов в предлоение отличается, то это разные предлоения
    if (len(test) == len(test2)):

        # Задаем временные переменные
        tmp = [] # Переменная нужна для перефоратирования предложения
        count = (len(test) + 1) # Используется для высчитытования процента ошибки.
        encorect = 1 # Счетчик ошибок

        for i in range(len(test)): # Получаем количества слов
            if (test[i] != test2[i]): # Проверяем, что слова отличаются
                print(test[i] + "\t\t" + test2[i] + "\t false")

                if (100 / count * encorect) < procent_error: # Проверяем процент отличия слов в предложение
                    encorect = encorect + 1 # Если слова отличаются, то увиличиваем процент отличая сообщения
                    tmp.append(test[i]) # Во временный массив добавляем вместо слова, которая отличается символ *
                else:
                    return test # Если процент отличая высокий, то остановить обработку и вернуть пустое значение

            else: # Если слова одинаковые
                print(test[i] + "\t\t" + test2[i] + "\t true")
                tmp.append('*')  # Во временную переменную добавить слова из объекта

        return tmp # Вернуть список слов

    else:
        return test