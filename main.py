import requests
import pprint



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
    print("Содержимое ответа:")
    pprint.pprint(json_data)
else:
    print("Ошибка при получении данных.")
