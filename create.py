import model.test

procent_error = 30


def examination_poof(poof, queue_vectors):
    poof1 = ''

    for vector in queue_vectors:
        if (len(poof.get_word()) == len(vector.get_end().get_word()) and
                (100 / (len(poof.get_word()) + 1) * len(list(set(poof.get_word()) - set(vector.get_end().get_word()))) < procent_error)):
            list_data = compare_words(poof.get_word(), vector)
            vector.get_end().update_data(list_data)
            poof1 = vector.get_end()
            poof = poof1
    queue_vectors.append(model.vector.Vector(queue_vectors[-1].get_end(), poof))



def compare_words(poof, vector):
    tmp = []  # Переменная нужна для перефоратирования предложения
    count = (len(poof) + 1)  # Используется для высчитытования процента ошибки.

    for i in range(len(poof)):  # Получаем количества слов

        if (poof[i] == vector.get_end().get_word()[i]) or (vector.get_end().get_word()[i] == '*'):  # Проверяем, что слова отличаются
            # print(poof[i] + "\t\t" + vector.get_end().get_word()[i] + "\t true")
            tmp.append(poof[i])

        elif (poof[i] != vector.get_end().get_word()[i]):
            # print(poof[i] + "\t\t" + vector.get_end().get_word()[i] + "\t false")
            tmp.append('*')  # Во временную переменную добавить слова из объекта
    # print(tmp, compare_words)
    return tmp