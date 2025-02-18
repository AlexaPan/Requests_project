# Задание 1: Получение данных
#
# Импортируйте библиотеку requests.
#
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
#
# Распечатайте статус-код ответа.
#
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

"""

# URL для поиска репозиториев на GitHub с языком HTML
url = 'https://api.github.com/search/repositories'
params = {
    'q': 'language:HTML',  # Параметр для поиска репозиториев с кодом HTML
    'sort': 'stars',        # Сортировка по количеству звезд
    'order': 'desc'        # Порядок сортировки (по убыванию)
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print(f"Статус-код ответа: {response.status_code}")

# Печать содержимого ответа в формате JSON
if response.status_code == 200:
    json_data = response.json()
    print("length: ", len(json_data))
    print("Содержимое ответа:")
    pprint.pprint(json_data)
else:
    print("Ошибка при получении данных.")
"""
# Задание 2: Параметры запроса
#
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#
# Отправьте GET-запрос с параметром userId, равным 1.
#
# Распечатайте полученные записи.


"""

# URL API с возможностью фильтрации по userId
url = 'https://jsonplaceholder.typicode.com/posts'

# Параметры запроса: фильтрация по userId = 1
params = {
    'userId': 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Преобразование ответа в JSON
    posts = response.json()

    # Печать полученных записей
    for post in posts:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print('-' * 40)

    # Печать количества полученных записей
    print(f"Количество записей: {len(posts)}")

    #print in json format
    print("In json format:")
    pprint.pprint(posts)
else:
    print(f"Ошибка при запросе: {response.status_code}")
"""

# Задание 3: Отправка данных
#
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
#
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
#
# Отправьте POST-запрос с этими данными.
#
# Распечатайте статус-код и содержимое ответа.
#
# В поле для ответа загрузи скриншоты сделанных заданий или ссылку на Git.

import requests
from pprint import pprint  # Для красивого вывода ответа

# URL API для создания нового поста
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода и содержимого ответа
print(f"Статус-код ответа: {response.status_code}")
print("Содержимое ответа:")
pprint(response.json())
print(f"Количество записей: {len(response.json())}")