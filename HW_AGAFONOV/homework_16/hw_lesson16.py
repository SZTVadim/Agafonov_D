# В вашем репозитории уже есть файл data_test/application.log.
#
# Напишите функцию, которая принимает тип записи ("ERROR", "WARNING", "INFO"),
# открывает файл через with open(...), построчно читает его и выводит только строки с переданным типом.
# Для проверки вызовите find_log_entries("ERROR").
def type_log(typet):
    with open("data_test/application.log", "r") as file:
        for line in file:
            if typet in line:
                print(line.strip())


type_log("ERROR")
