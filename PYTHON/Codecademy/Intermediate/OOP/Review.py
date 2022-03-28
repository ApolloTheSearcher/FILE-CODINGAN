from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1
    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod # => Abstraction
    def say_id(self):
        pass
    
class User:
    def __init__(self): 
        self._username = None

    @property
    def username(self):
        pass
    @username.getter # => Getter decorator
    def username(self): 
        return self._username # => Getter

    @username.setter # => Setter decorator
    def username(self, new_name):
        self._username = new_name # => Setter
    # self._username(Protected)

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee): # => DunderMethod
        print("{} added.".format(employee.username))
        self.attendees.append(employee.username)

    def __len__(self):
        return len(self.attendees)

class Employee(AbstractEmployee, User):
    def __init__(self, username):
        super().__init__()
        User.__init__(self) # Untuk mengganti isi dari parameter username pada method __init__ di class User
        self.username = username # yang tadinya pada method __init__ di class User isinya None diubah menjadi username

    def say_id(self):
        print("My id is {}".format(self.id))

    def say_username(self):
        print("My username is {}".format(self.username))