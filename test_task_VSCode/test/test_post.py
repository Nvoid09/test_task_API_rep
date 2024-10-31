import requests


url = 'http://127.0.0.1:8000/process_csv'
files = {'file': ('data_changed_2_strings.csv', open(
    'test/data_changed_2_strings.csv', 'rb'), 'text/csv')}
response = requests.post(url, files=files)
print(response.json())  # Выводит JSON-ответ с результатами
