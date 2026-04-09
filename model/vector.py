# Класс вектор нужна для построене последовательности.
class Vector:

    def __init__(self, start, end):
        self.start = start # в переменную записывается данные
        self.end = end

    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end