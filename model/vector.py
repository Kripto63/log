class Vector:

    def __init__(self, data):
        self.data = data
        self.vector = []

    def get_data(self):
        return self.data
    
    def get_after(self):
        return self.after
    
    def add_vector(self, obj):
        self.vector.append(obj)