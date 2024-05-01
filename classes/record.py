from abc import ABC, abstractmethod
from classes import Name, Phone, Birthday, PhoneFindError


class AbstractRecord(ABC):
    @abstractmethod
    def add_phone(self, value):
        pass

    @abstractmethod
    def remove_phone(self, value):
        pass

    @abstractmethod
    def edit_phone(self, old_value, new_value):
        pass

    @abstractmethod
    def find_phone(self, value):
        pass

    @abstractmethod
    def add_birthday(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass


class Record(AbstractRecord):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, user_phone):
        self.phones.append(Phone(user_phone))


    def remove_phone(self, user_phone):
        if any(str(phone) == user_phone for phone in self.phones):
            self.phones = [phone for phone in self.phones if str(phone) != user_phone]
        else:
            raise PhoneFindError(f"Phone {user_phone} can`t be removed. Looks like it does not exist")


    def edit_phone(self, old_phone, new_phone):
        if any(str(phone) == old_phone for phone in self.phones):
            for phone in self.phones:
                if str(phone) == old_phone:
                    target_index = self.phones.index(phone)
                    self.phones[target_index] = Phone(new_phone)
        else:
            raise PhoneFindError(f"Phone {old_phone} can`t be edited. Looks like it does not exist")
                 

    def find_phone(self, user_phone):
        phone_to_find = [phone for phone in self.phones if str(phone) == user_phone]
        
        if len(phone_to_find) > 0:
             return phone_to_find[0]
        else:
            raise PhoneFindError(f"Phone {user_phone} can`t be find. Looks like it does not exist.")
        

    def add_birthday(self, value):
        self.birthday = Birthday(value)


    def __getitem__(self, value):
        if value == 'name':
            return self.name
        if value == 'phones':
            return self.phones
        if value == 'birthday':
            return self.birthday
        

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"