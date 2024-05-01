import pickle
from classes import AddressBook

class FileManager:
    def __init__(self, filename="addressbook.pkl"):
        self.filename = filename

    def save_data(self, book: AddressBook):
        with open(self.filename, 'wb') as file:
            pickle.dump(book, file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()
            



