import hashlib

class Hash_word:
    
    def __init__(self, words):
        self.d = { 'words': words.split(" "),
            'list_hex_words': self.__set_list_hex_word(words),
            'hex': hash(tuple(words)),
            }

    # Приоброзование массива строк в массив хешей
    def __set_list_hex_word(self, words):
        list_hex_word = []
        list_words = words.split(" ")
        for i in list_words:
            word_bytes = i.encode('UTF-8')
            hashlib.sha256(word_bytes)
            hash_obj = hashlib.sha256(word_bytes)
            hex_hash = hash_obj.hexdigest()
            list_hex_word.append(hex_hash)
        return list_hex_word


    def get_list_hex_word(self):
        return self.d["list_hex_words"]
    
    
    def get_word(self):
        return self.d["words"]
    
    
    def get_word_by_hex_word(self, hex):
        index_word = self.d["list_hex_words"].index(hex)
        return self.d['words'][index_word]
    
    def get_hex(self):
        return self.d['hex']


            