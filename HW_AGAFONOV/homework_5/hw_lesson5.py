# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
print(fruits)
fruits.extend(["апельсин", "груша"])
print(fruits)
fruits.insert(1, "виноград")
print(fruits)

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
print(fruits)
delete_fruit = fruits.pop()
print(delete_fruit)

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
