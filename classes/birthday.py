from datetime import datetime
from classes import Field
from classes import BirthdayError


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value


    @property
    def value(self):
        return self.__value
    

    @value.setter
    def value(self, value):
        print('value',datetime.now(), value)
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')                    
        except ValueError:
            raise BirthdayError("Invalid date format. Use birthday date in format DD.MM.YYYY.")
        
        if birthday >= datetime.today():
            raise BirthdayError(f'Birthday date cannot be in a future.')
        
        self.__value = birthday.date()
 

    def __getitem__(self):
        return self.value 
    

    def __str__(self):
        return f"{self.value.strftime('%Y.%m.%d')}"