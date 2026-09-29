# Адрес сваггера https://petstore.swagger.io/#
#
# Для ДЗ использовать клиента pet (группа запросов pet)
#
#
# Выполнить запрос Post
# Выполнить запрос Get
# Выполнить запрос Put
# Выполнить запрос Delete

import requests

# создание животнго
response_1 = requests.post("https://petstore.swagger.io/v2/pet",
                           json={
                               "id": 64792,
                               "category": {
                                   "id": 1,
                                   "name": "Коты"
                               },
                               "name": "Мурзик",
                               "photoUrls": [
                                   "string"
                               ],
                               "tags": [
                                   {
                                       "id": 0,
                                       "name": "Уличный"
                                   }
                               ],
                               "status": "available"
                           })
print(f"Статус-код: {response_1.status_code}")
# возврат животного
response_2 = requests.get("https://petstore.swagger.io/v2/pet/64792")
print(f"Статус-код: {response_2.status_code}")
# замена животного
response_3 = requests.put("https://petstore.swagger.io/v2/pet",
                          json={
                              "id": 64792,
                              "category": {
                                  "id": 1,
                                  "name": "Cобака"
                              },
                              "name": "Мурзик",
                              "photoUrls": [
                                  "string"
                              ],
                              "tags": [
                                  {
                                      "id": 0,
                                      "name": "Домашний"
                                  }
                              ],
                              "status": "available"
                          })
print(f"Статус-код: {response_3.status_code}")
# удаление животного
response_4 = requests.delete("https://petstore.swagger.io/v2/pet/64792")
print(f"Статус-код: {response_4.status_code}")
