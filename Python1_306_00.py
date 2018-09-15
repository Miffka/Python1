import requests

"""r = requests.get("http://example.com") #простой GET запрос
print(r.text) #вывод ответа от сервера"""

url = "http://example.com"
par = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params = par) # передача параметров в запрос
print(r.url) #сформированный url-адрес у учетом параметров GET запроса
print(r.content) #получение всего содержимого страницы

"""
url = "http://httpbin.org/cookies"
cookies = {"cookies_are": "working"}
r = requests.get(url, cookies = cookies) #отправка сформированных cookies на сервер
print(r.text)

print(r.cookies["example_cookie_name"]) #использование cookies, полученных от сервера
"""

