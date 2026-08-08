# ЗАДАНИЕ 1: Список и list comprehension
temps = [18, 22, -3, 25, 19, -1, 21]
new_temp_list = [C * 9/5 + 32 for C in temps]
print(new_temp_list)

# ЗАДАНИЕ 2: Словарь и dict comprehension
users = {
     "ivan": "qwerty",
     "maria": "12345",
     "petr": "admin",
     "anna": "pass",
     "guest": "guest"
 }
new_dict = {login: len(password) for login, password in users.items()}
print(new_dict)


# ЗАДАНИЕ 3: Кортеж и tuple(...)
scores = (10, 7, 0, 9, 8, 5)
change_score = tuple(score * 1.1 for score in scores)
print(change_score)