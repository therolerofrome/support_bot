import requests

token = ""

# Получаем тикеты
url = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/ticket'



session = requests.Session()
session.headers.update({
    'Authorization': f'Bearer {token}'
})

response = session.get(url)
print(response)
print(response.text)


#получаем инфу о пользователе
url2 = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/user'

response2 = session.get(url2)

print(response2)
print(response2.text)
