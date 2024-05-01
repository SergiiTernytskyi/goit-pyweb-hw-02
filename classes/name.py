from classes import Field

class Name(Field):
    def __init__(self, value: str):
        self.value = value

    def __getitem__(self):
        return self.value
        
    def __str__(self):
        return f'{self.value}'