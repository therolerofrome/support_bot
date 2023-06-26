import json

import requests

token = ""

# Получаем тикеты
url = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/ticket'



session = requests.Session()
session.headers.update({
    'Authorization': f'Bearer {token}',

})

response = session.get(url)
print(response)
print(response.json)


#получаем инфу о пользователе
url2 = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/user'

response2 = session.get(url2)

print(response2)
print(response2.json)



# Создаем тикет
url3 = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/ticket'

data ={
  "typeId": "ff8e4a2c-4096-499c-8e44-9e31f3d49f2e",
  "theme": "ТЕСТ_ТЕМА_ЗАПРОС",
  "description": "Описание_тест_запрос",
  "environmentId": "514a4b1e-edd7-4e73-b0aa-098055d7d8a6",
  "systemId": "1af428dd-7cdc-4e9d-96fe-1bbc7adcafe9",
  "ticketPriority": "NONE"
}



response3 = session.post(url3, data=json.dump(data), headers={
    'Content-type': 'application/json',
    'Accept': 'application/json',
})

print(response3)
print(response3.json)


