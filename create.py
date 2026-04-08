# import model.test.Hash_word as hw
import model.test

procent_error = 30

# def create(after_poof, now_poof):
#     after = hw(after_poof)
#     now = hw(now_poof)
#
#     print(hw)


def comparison_poof(test, test2, poof) -> list:
    if (len(test) == len(test2)):
        list_hex_word = []
        count = (len(test) + 1)
        encorect = 1

        for i in range(len(test)):

            if (test[i] != test2[i]):
                print(test[i] + "\t" + test2[i] + "\t false")

                if (100 / count * encorect) < procent_error:
                    encorect = encorect + 1
                    list_hex_word.append('*')
                else:
                    return

            else:
                print(test[i] + "\t" + test2[i] + "\t true")
                list_hex_word.append(poof.get_word_by_hex_word(test[i]))

    return list_hex_word