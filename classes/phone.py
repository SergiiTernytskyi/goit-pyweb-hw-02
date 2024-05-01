import re
from classes import Field
from classes import PhoneVerificationError

class Phone(Field):
    def __init__(self, value: str):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if not re.fullmatch(r'(\+?38)?\d{10}', value):
            raise PhoneVerificationError(f'Wrong phone number format: {value}')
        
        self.__value = value

    def __getitem__(self):
        return self.value
    
    def __str__(self):
        return f'{self.value}'
            
