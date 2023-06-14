import requests

data = {"custname": "bane",
        'custtel': 'parol',
        'custemail': 'snaiper1731@mail.ru',
        'size': 'small',
        'topping': 'bacon',
        'delivery': '18:00',
        'comments': 'doaosddss'}

data3 = {'session_code': 'cBzhS4_YewBZmusi1pCtEy9b8vz7Ru2crjRi_EByFQE',
         'execution': '2d1c4e91-4f13-4589-a025-9a9e4dd5e97e',
         'client_id': "frontapp",
         'tab_id': 'ka2B7NKQtKo'}

data4 = 
{
    "priorities": [
      "NONE"
}

data5 = {
    'username' : '',
    "password" : '',
}
            
data6 = {
"theme" : " ",
"description" : " "
    ## Спарсить через сеть поле среды, когда мы сможем создавать пост
}
            
            
token = 'c170af50-1a63-46a0-8b5a-5da9156ceb52'
url = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/tickets/'
url1 = 'http://external-integration.dev.t1support-portal.dev.ts/get'
url2 = 'https://httbin.org/post'
url3 = 'http://keycloak.t1support-portal.dev.ts:8080/auth/realms/T1-Support-Portal/login-actions/authenticate?session_code=J_8Y5-3CPLhDmTCSv7KOHas66HFDUFJysLPgmhcKnoA&execution=2d1c4e91-4f13-4589-a025-9a9e4dd5e97e&client_id=frontapp&tab_id=D6suZWoL_jU'
url4 = 'http://fe.dev.t1support-portal.dev.ts/tickets'
url5 = 'http://fe.dev.t1support-portal.dev.ts/knowledge-base'
            
params = {
    "theme": "string",
    "numberFrom": 0,
    "numberTo": 0,
    "statuses": [
        "NEW"
    ],
    "priorities": [
        "NONE"
    ],
    "specialistIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "contractIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "systemIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "workGroupIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "tagIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "clientIds": [
        "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "tagName": "string",
    "clientName": "string",
    "specialistName": "string",
    "systemName": "string",
    "dateSolveFrom": "2023-14-05T09:06:28.932Z",
    "dateSolveTo": "2023-14-05T09:06:28.932Z"
}

headers = {'Authorization': 'Bearer ' + token}

headers2 = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6489ac62-1d21311b2bcd3b811ddbd22d"
}



response = requests.get(url4, headers=headers2, data=data5)
response1 = requests.get(url5, headers=headers2)
print(response)
print(response1)
