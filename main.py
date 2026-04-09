import re
import model.test
import model.vector
from create import examination_poof

def creating_first_vector():
    start = model.test.Hash_word('START')
    queue_vector.append(model.vector.Vector(0, start))


if __name__ == '__main__':
    queue_vector = []
    creating_first_vector()

    patern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|DEBUG|WARN|ERROR) (\[.*\] .*)'

    with open('test_log.txt', 'r') as f:
        file_log = re.findall(patern, f.read())

    for i in file_log:
        poof = model.test.Hash_word(i[2])
        examination_poof(poof, queue_vector)

    # # Создание объекта Hash_word и присваение строки
    # poof = model.test.Hash_word(words)

    # # в переменную test помещаем масив хэшей
    # test = poof.get_list_hex_word()
    # test2 = model.test.Hash_word(words2).get_list_hex_word()

    # examination_poof(test, test2, poof, f)

    # print(f)

    print('---------------')
    print('---------------')
    print('---------------')

    for i in queue_vector:
        try:
            print('----------------')
            print(f'{i.get_start().get_word()} {i.get_start()} => {i.get_end().get_word()} {i.get_end()}')
        except AttributeError:
            print()


