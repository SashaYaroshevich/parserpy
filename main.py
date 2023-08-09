import requests

link = "https://icanhazip.com/"
link2 = "https://browser-info.ru/"
responce = requests.get(link).text
responce2 = requests.get(link2).text
print(responce)
print(responce2)

with open("l.html", "w", encoding="utf-8") as file:
    file.write(responce2)