# ЗАДАНИЕ 1: Работа с типами данных
check_string = "Привет"
check_integer = 42
check_float = 3.14
check_list = [1, 2, 3]

print(type(check_string))
print(type(check_integer))
print(type(check_float))
print(type(check_list))

# ЗАДАНИЕ 2: Преобразование регистра строк

text_register = "python PROGRAMMING"
print(text_register.lower())
print(text_register.upper())
print(text_register.capitalize())
print(text_register.title())

# ЗАДАНИЕ 3: Удаление пробелов

delete_space = " Hello World "
print(delete_space.strip())
print(delete_space.lstrip())
print(delete_space.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк

text_task_4 = "яблоко,банан,апельсин,груша"
text_task_4_1 = text_task_4.split(",")
text_task_4_2 = "|".join(text_task_4_1)
print(text_task_4_1)
print(text_task_4_2)


# ЗАДАНИЕ 5: Замена подстрок

text_task_5 = "Я изучаю Python. Python - это круто!"
change_5 = text_task_5.replace("Python", "Java")
print(change_5)

# ЗАДАНИЕ 6: Поиск и подсчет
text_task_6 = "Python программирование на Python"
print(text_task_6.find("Python"))
print(text_task_6.count("Python"))
print(text_task_6.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# ЗАДАНИЕ 8: Срезы строк
text_task_8 = "Python very good"
print(text_task_8[:3:])
print(text_task_8[13::])
print(text_task_8[::2])
print(text_task_8[::-1])

# ЗАДАНИЕ 9: Экранирование символов
text_task_9 = "Он сказал: \"Привет\""
text_task_9_1 = "Первая строка\nВторая строка"
print(text_task_9)
print(text_task_9_1)


