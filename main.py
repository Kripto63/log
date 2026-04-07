import hashlib
import model.test
import model.vector

procent_error = 30


def comparison_poof(test, test2) -> list:
    
    if (len(test) == len(test2)):
        list_hex_word = []
        count = (len(test)+1)
        encorect = 1
        
        for i in range(len(test)):
            
            if (test[i] != test2[i]):
                print(test[i] + "\t" + test2[i] + "\t false")
                
                if (100/count*encorect) < procent_error:
                    encorect = encorect + 1
                    list_hex_word.append('*')
                else:
                    return
                
            else:
                print(test[i] + "\t" + test2[i] + "\t true")
                list_hex_word.append(poof.get_word_by_hex_word(test[i]))
                
    return list_hex_word



if __name__ == '__main__':
    f = []
    words = 'word text to1 file1 not1 did casel1'
    words2 = 'word text to file1 not1 to casel1'

    
    poof = model.test.Hash_word(words)
    test = poof.get_list_hex_word()
    # test.get_list_hex_word()
    test2 = model.test.Hash_word(words2).get_list_hex_word()
    # test2.get_list_hex_word()
    
    try:
        
        list_hex_word = comparison_poof(test, test2)
        poof = model.test.Hash_word(" ".join(list_hex_word))
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


    print(f)
    

