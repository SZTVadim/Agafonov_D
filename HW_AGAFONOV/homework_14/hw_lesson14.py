# ЧАСТЬ 1: Абстракция - Абстрактный класс Animal
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# ЧАСТЬ 2: Наследование - Классы Dog и Cat
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


# ЧАСТЬ 3: Инкапсуляция - Класс Zoo (Зоопарк)
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals


# ЧАСТЬ 4: Полиморфизм - Работа с разными животными
def animal_sound(animal):
    animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

# У нас уже есть в классах dog и cat методы make.sound, с помощью
# метода animal_sound мы можем обратиться к любому
# классу и вызовется метод, который есть в классе animal_sound,
# а именно make_sound()

zoo = Zoo("Городской зоопарк")
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# animal = Animal()
# произошла ошибка, Animal это абстрактный класс, и
# в нем мы не реализовали метод make_sound(),
# без запуска которго у нас упадет все с ошибкой
