import model.test

procent_error = 30

def examination_poof(test, test2, poof, f):
    try:
        
        list_hex_word = comparison_poof(test, test2, poof) # Вызвать функцию проверки предложения
        poof = model.test.Hash_word(" ".join(list_hex_word)) # Строку преобрзовать объект Hash_word
        print('----')
        print(poof.d['words'])

    except UnboundLocalError:
        print("Размер списков отличается")

    except TypeError:
        print("Строки отличатся")

    if poof in f:
        print(f)
    else:
        f.append({poof.get_hex(): poof})

def comparison_poof(test, test2, poof) -> list:
    # если количество слов в предлоение отличается, то это разные предлоения
    if (len(test) == len(test2)):

        # Задаем временные переменные
        list_hex_word = [] # Переменная нужна для перефоратирования предложения
        count = (len(test) + 1) # Используется для высчитытования процента ошибки.
        encorect = 1 # Счетчик ошибок

        for i in range(len(test)): # Получаем количества слов
            if (test[i] != test2[i]): # Проверяем, что слова не отличаются
                print(test[i] + "\t" + test2[i] + "\t false")

                if (100 / count * encorect) < procent_error: # Проверяем процент отличия слов в предложение
                    encorect = encorect + 1 # Если слова отличаются, то увиличиваем процент отличая сообщения
                    list_hex_word.append('*') # Во временный массив добавляем вместо слова, которая отличается символ *
                else:
                    return # Если процент отличая высокий, то остановить обработку и вернуть пустое значение

            else:
                print(test[i] + "\t" + test2[i] + "\t true")
                list_hex_word.append(poof.get_word_by_hex_word(test[i])) # Во временную переменную добавить слова из объекта

    return list_hex_word # Вернуть спсок слов