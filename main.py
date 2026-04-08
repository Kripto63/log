import re

import model.test
import model.vector
from create import examination_poof


if __name__ == '__main__':
    f = []

    patern = r'(\[\d{4}\-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]) (INFO|DEBUG): (.*)'

    with open('test_data.txt', 'r') as f:
        file_log = re.findall(patern, f.read())

    for s in file_log:
        print(s)


    # # Создание объекта Hash_word и присваение строки
    # poof = model.test.Hash_word(words)
    #
    # # в переменную test помещаем масив хэшей
    # test = poof.get_list_hex_word()
    # test2 = model.test.Hash_word(words2).get_list_hex_word()
    #
    # examination_poof(test, test2, poof, f)
    #
    # print(f)
    

