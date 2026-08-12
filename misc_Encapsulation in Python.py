# Encapsulation - hiding a class's internal details and exposing only what is
# necessary to prevent accidental modification

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # private attribute

    def get_balance(self):
        return self.__balance

account = BankAccount(8000)
print(account.get_balance(), end = '\n\n') #access through method
# print(account.__balance) - cannot access directly

# naming conventions
class Person1:
    def __init__(self):
        self.name = "Cess" # public
        self._age = 26 # protected (can access within the same class or subclass,
        # not advisable to use in external classes)
        self.__ssn = '012-34-5678' # private (you can access them only within the class itself)

ali = Person1()
print(ali.__dict__, end = '\n\n')

class Person:

    def __init__(self, field, age):
        self.field = field
        self.age = age

    def increase_age(self, increment):
        self.age += increment
        return f"New age: {self.age}"

oliver = Person('Data Science', 22) #it is an INSTANCE OF THE CLASS

print(oliver.field)
print(oliver.age)

incr = oliver.increase_age(67)
print(incr)
print(oliver.age)

oliver.field = 'Classics'
oliver.age = 24

print(oliver.age)
print(oliver.field, end = '\n\n')


class Employee:

    def __init__(self, name, year_of_service):
        self.name = name
        self._year_of_service = year_of_service
        # protected member of class

    def _calculate_bonus(self): # protected method
        return self._year_of_service * 0.1

emp = Employee('Ali', 14)

print(emp._year_of_service)
print(emp._calculate_bonus(), end = '\n\n' )


class SecureVault:

    def __init__(self, password):
        self.__password = password # private attribute

    def verify_password(self, attempt):
        return self.__password == attempt

    def __internal_security_check(self): # private method
        print('Runnig security check...')
        return True

vault = SecureVault(228228)

print(vault.verify_password(223223))
print(vault.verify_password(228228), end = '\n\n')

# print(vault._SecureVault__password) - don't use this way

class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value): # says what happens when you assign a value to a
        # property, lets u change
        if value > 0:
            self._age = value

person = Person(27)
print(person.age)

person.age = 50
print(person.age, end = '\n\n')

# financial calculations and transactions
class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            self.__record_transaction('deposit', amount)
            return True
        return False

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__record_transaction('withdrawal', amount)
            return True
        return False

    # method to keep the logs:
    def __record_transaction(self, transaction_type, amount):

        self.__transaction_history.append({
            'type': transaction_type,
            'amount':amount
            }
        )

    @property
    def balance(self):
        return self.__balance

account = BankAccount('441 285 731', 10000)
account.deposit(1498)
account.withdraw(980)
account.withdraw(228)
print(f'Account {account.account_number} balance: ${account.balance}')
print(account._BankAccount__transaction_history, end = '\n\n')

# game character  state management
class GameChar:

    def __init__(self, name, health = 100):
        self.name = name
        self.__health = health
        self.__max_health = health

    @property
    def health(self):
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount )

    def heal(self, amount):
        self.__health = min(self.__max_health, self.__health + amount)

hero = GameChar('Agamemnon')

hero.take_damage(30)
print(hero.health)

hero.heal(123)
print(hero.health, end = '\n\n')


class APIClient:

    def __init__(self, api_key):
        self.__api_key = api_key
        self._base_url = "https://api.learn.com"
        self._timeout = 30

    def make_request(self, endpoint):

        """public method to make API request"""

        headers = self.__get_auth_headers()
        return f'Request to {self._base_url}/{endpoint} with auth headers'

    def __get_auth_headers(self):

        """securely formats authentication headers"""

        return {"Authorization": f'Bearer {self.__api_key}'}

client = APIClient("secret_api_key_55775")
print(client.make_request('users'))

# setter - проверяет значение на вход которое дали
# getter - решает в каком виде отдать

# property - совокупность сеттера и геттера





