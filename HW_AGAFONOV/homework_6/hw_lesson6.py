student = {
    "имя" : "Иван",
    "возраст" : 20,
    "курс" : 2,
    "город" : "Москва"
}
print(student.keys())
print(student.values())
for key,value in student.items():
    print(f"Ключ: {key}, Значение: {value}")

for value in student.values():
    print(f"Значение: {value}")

# ЗАДАНИЕ 2: Объединение словарей

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = student1 | student2
print(student3)
student1.update(student2)
print(student1)
print(student2)
print(student3)
