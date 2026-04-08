import hashlib
import model.test
import model.vector
from create import examination_poof


if __name__ == '__main__':
    f = []
    words = 'word text to1 file1 not1 did casel1'
    words2 = 'word text to file1 not1 to casel1'

    # Создание объекта Hash_word и присваение строки
    poof = model.test.Hash_word(words)

    # в переменную test помещаем масив хэшей
    test = poof.get_list_hex_word()
    test2 = model.test.Hash_word(words2).get_list_hex_word()

    examination_poof(test, test2, poof, f)

    print(f)
    

