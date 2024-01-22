from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.valid_phone()

    def valid_phone(self):
        if not (isinstance(self.value, str) and self.value.isdigit() and len(self.value) == 10):
            raise ValueError('Invalid phone number')
     
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number:str):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number:str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return

    def find_phone(self, phone_number:str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
    
  
    def edit_phone(self, old_phone:str, new_phone:str):
        for phone in self.phones:
            if phone.value == old_phone:
                if not (new_phone.isdigit() and len(new_phone) == 10):
                    raise ValueError('Invalid phone number')
                else:
                    phone.value = new_phone
                return
        raise ValueError('Invalid phone number')

            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value]=record

    def find(self, name:str):
        if name in self.data:
            return self.data[name]
        
    def delete(self, name:str):
        if name in self.data:
            del self.data[name]

book = AddressBook()

