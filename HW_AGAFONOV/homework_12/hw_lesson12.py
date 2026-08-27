# ЗАДАНИЕ 1: Класс Book (Книга)
class Book:

    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"\'{self.title}' автор {self.author}, {self.pages} стр"

    def is_long(self):
        return self.pages > 300


book_1 = Book("Война и мир" , "Толстой",  900)
book_2 = Book("Гарри Поттер" , "Роулинг", 401)
book_3 = Book("Красная шапочка" , "Шарль Перро", 100)
print(book_1.get_info())
print(book_1.is_long())
print(book_2.get_info())
print(book_2.is_long())
print(book_3.get_info())
print(book_3.is_long())

# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


money = BankAccount("Игорь", 1500)
print(money.withdraw(1499))
print(money.get_balance())
print(money.withdraw(1501))
print(money.get_balance())
