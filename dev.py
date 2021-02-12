
class User(object):
    def __init__(self, name):
        self.name = name
    def out_name(self):
        print(self.name)
    
    @staticmethod
    def out_ok():
        print("ok")

class Student(object):
    def __init__(self, id):
        self.id = id
    @classmethod
    def create_student(cls, id):
        return cls(id)
        






