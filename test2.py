import requests




token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZMVZRaHk0a2FlM1FGZ0JTRFh0TTgtY0tyc1l5Z0tXcGFJUjdWUnlmeXJFIn0.eyJleHAiOjE2ODcxODUxOTYsImlhdCI6MTY4NzE3MzE5NiwianRpIjoiMmM5NmFhMTUtZjMyYi00ZDMyLTllMTctZDRjM2M4OWYxYTIxIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLnQxc3VwcG9ydC1wb3J0YWwuZGV2LnRzOjgwODAvYXV0aC9yZWFsbXMvVDEtU3VwcG9ydC1Qb3J0YWwtUmVsZWFzZSIsInN1YiI6Ijc5MzJhNjY5LWRhYzItNGM4NS1iZDE5LTg1NDdkZWQ2ODY4MSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZyb250YXBwIiwic2Vzc2lvbl9zdGF0ZSI6ImRmNGNhN2Q1LTE5NjItNDBiMi04NTRmLWUxNjIzMzkzOTA1ZSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsi0JLQotCRINGA0YPQutC-0LLQvtC00LjRgtC10LvRjCAxIl19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjRjYTdkNS0xOTYyLTQwYjItODU0Zi1lMTYyMzM5MzkwNWUiLCJvcmdhbml6YXRpb25fdGl0bGUiOiLQkNC00LzQuNC9INC-0YDQs9Cw0L3QuNC30LDRhtC40Y8iLCJidXNpbmVzc191c2VyX2lkIjoiOThiYTM3YTYtNThjNi00NDcyLTk4OWMtYTMzOGI3YmI0YzI3IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoi0JjQstCw0L0g0JjQstCw0L3QvtCyIiwicGhvbmVfbnVtYmVyIjoiKzcgKDIyMikgMzIzLTIyLTExIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaXZhbm92IiwibWlkZGxlX25hbWUiOiLQkNC90LTRgNC10LXQstC40YciLCJnaXZlbl9uYW1lIjoi0JjQstCw0L0iLCJmYW1pbHlfbmFtZSI6ItCY0LLQsNC90L7QsiIsImVtYWlsIjoiaXZhbm92QGl2YW5vdi5ydSJ9.SR177g7VUKBmaSLr-l3w3qRVzoo0n_y_tw2Q34N13Hr9nch1YYV4GQHdSxWJSDlAEH04ham9_DNA1fF1KSW7CBdA61qS_s405_WSudbbR4-xoTlLZzRZI6XMLqFTDJ03U7t1Be8aEI4IxFdmihZ_QVGkkeCVpT1QC0vReryWllxv-EZXEZmlRTDd5D3hF6NqI7PJrfPhmMEfXcA0wLH_Urc27j5oKtvH6MrJcGOQTZuZae_wojTcAJan1g-0To6Wk3mICT_q6KVDxAEmGCfoUT4USnp1aA6X9r7_SPba9Z7avMy_17asBFutGpi3AoiaY9_8HKLcyZr1U36mqL2DqQ"

BASE_URL = f'https://keycloak.supportal.t1-consulting.ru/auth/realms/T1-Support-Portal/protocol/openid-connect/{token}'

BASE_URL2 = f'http://fe.dev.t1support-portal.dev.ts'

BASE_URL3 = f'http://ticket.dev.t1support-portal.dev.ts'

url = f'https://keycloak.supportal.t1-consulting.ru/auth/realms/T1-Support-Portal/protocol/openid-connect/{token}'
url2 ='http://ticket.dev.t1support-portal.dev.ts/api/ticket'
url3 = 'http://fe.dev.t1support-portal.dev.ts/api/v1/ticket/token'

url4 = f'https://keycloak.supportal.t1-consulting.ru/auth/realms/T1-Support-Portal/protocol/openid-connect/{token}/api/v1/user'


user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/75.0.3770.142 Safari/537.36'

headers = {'Authorization': 'Bearer ' + token}
headers2 = {'Authorization': token}
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZMVZRaHk0a2FlM1FGZ0JTRFh0TTgtY0tyc1l5Z0tXcGFJUjdWUnlmeXJFIn0.eyJleHAiOjE2ODcxODUxOTYsImlhdCI6MTY4NzE3MzE5NiwianRpIjoiMmM5NmFhMTUtZjMyYi00ZDMyLTllMTctZDRjM2M4OWYxYTIxIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLnQxc3VwcG9ydC1wb3J0YWwuZGV2LnRzOjgwODAvYXV0aC9yZWFsbXMvVDEtU3VwcG9ydC1Qb3J0YWwtUmVsZWFzZSIsInN1YiI6Ijc5MzJhNjY5LWRhYzItNGM4NS1iZDE5LTg1NDdkZWQ2ODY4MSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZyb250YXBwIiwic2Vzc2lvbl9zdGF0ZSI6ImRmNGNhN2Q1LTE5NjItNDBiMi04NTRmLWUxNjIzMzkzOTA1ZSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsi0JLQotCRINGA0YPQutC-0LLQvtC00LjRgtC10LvRjCAxIl19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjRjYTdkNS0xOTYyLTQwYjItODU0Zi1lMTYyMzM5MzkwNWUiLCJvcmdhbml6YXRpb25fdGl0bGUiOiLQkNC00LzQuNC9INC-0YDQs9Cw0L3QuNC30LDRhtC40Y8iLCJidXNpbmVzc191c2VyX2lkIjoiOThiYTM3YTYtNThjNi00NDcyLTk4OWMtYTMzOGI3YmI0YzI3IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoi0JjQstCw0L0g0JjQstCw0L3QvtCyIiwicGhvbmVfbnVtYmVyIjoiKzcgKDIyMikgMzIzLTIyLTExIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaXZhbm92IiwibWlkZGxlX25hbWUiOiLQkNC90LTRgNC10LXQstC40YciLCJnaXZlbl9uYW1lIjoi0JjQstCw0L0iLCJmYW1pbHlfbmFtZSI6ItCY0LLQsNC90L7QsiIsImVtYWlsIjoiaXZhbm92QGl2YW5vdi5ydSJ9.SR177g7VUKBmaSLr-l3w3qRVzoo0n_y_tw2Q34N13Hr9nch1YYV4GQHdSxWJSDlAEH04ham9_DNA1fF1KSW7CBdA61qS_s405_WSudbbR4-xoTlLZzRZI6XMLqFTDJ03U7t1Be8aEI4IxFdmihZ_QVGkkeCVpT1QC0vReryWllxv-EZXEZmlRTDd5D3hF6NqI7PJrfPhmMEfXcA0wLH_Urc27j5oKtvH6MrJcGOQTZuZae_wojTcAJan1g-0To6Wk3mICT_q6KVDxAEmGCfoUT4USnp1aA6X9r7_SPba9Z7avMy_17asBFutGpi3AoiaY9_8HKLcyZr1U36mqL2DqQ"
query_params = {"api_key": api_key}

session = requests.Session()
response = session.get(url, headers = {
    'User-Agent': user_agent_val,
    'Authentication' : token
})


if response.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('1 ' + f'{response}')

response1 = requests.get(url2, params=query_params)

print(response1)

if response1.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('2 ' + f'{response1}')



response2 = requests.get(url2, headers=headers)

print(response2)

if response2.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('3 ' + f'{response2}')



response21 = requests.get(url2, headers=headers2)

print(response21)

if response21.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('4 ' + f'{response21}')

response3 = requests.get(url3, params=query_params)

print(response3)

if response3.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('5 ' + f'{response3}')

response4 = requests.get(url3, headers=headers)

print(response4)

if response4.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('6 ' + f'{response4}')

response41 = requests.get(url3, headers=headers2)

print(response41)

if response41.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('7 ' + f'{response41}')


response5 = requests.get(url4, headers=headers)

print(response5)

if response5.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('8 ' + f'{response5}')

response6 = requests.get(url4, headers=headers2)

print(response6)
if response6.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('9 ' + f'{response6}')

response7 = requests.get(url4, params=query_params)

print(response7)
if response7.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('10 ' + f'{response7}')

response8 = requests.get(f'{BASE_URL}/api/v1/user')

print(response8)

if response8.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('11 ' + f'{response8}')

response9 = requests.get(f'{BASE_URL2}/api/v1/user')

print(response9)

if response9.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('12 ' + f'{response9}')


response10 = requests.get(f'{BASE_URL3}/api/v1/tickets')

print(response10)

if response10.status_code != 200:
    print('Ошибка создания тикета: {}')
else:
    print('13 ' + f'{response10}')







url5 = 'http://keycloak.t1support-portal.dev.ts:8080/auth/realms/T1-Support-Portal/protocol/openid-connect/auth'
params = {
    'client_id': 'frontapp',
    'redirect_uri': 'http://fe.dev.t1support-portal.dev.ts/tickets',
    'state': '9e94fd6c-e4ac-4dc4-a32d-b02e7ade862d',
    'response_mode': 'fragment',
    'response_type': 'code',
    'scope': 'openid',
    'nonce': 'cca2e24c-29db-49b9-a470-e06057c9d53d',
    'code_challenge': 'AMhz9r4WqSA_QCECp1UIXGwsjeIe87v2yHNg8yVeU1M',
    'code_challenge_method': 'S256'
}

session1 = requests.Session()

response11 = session1.get(url5, params=params)

print(response11.text)


url6 = 'https://keycloak.supportal.t1-consulting.ru/auth/realms/T1-Support-Portal/protocol/openid-connect/token/api/v1/user'

session2 = requests.Session()

response12 = session1.get(url6)
print(response12)
print(response12.text)
print(response12.json())









url7 = f'http://fe.dev.t1support-portal.dev.ts/tickets' # использовать обычную ссылку
headers3 = {
    'Authorization': f'Bearer {token}'
}

session3 = requests.Session()

response12 = session3.get(url7, headers=headers3)
print(response12)
print(response12.text)
print(response12.json())

url8 = 'http://keycloak.t1support-portal.dev.ts:8080/auth/realms/T1-Support-Portal/protocol/openid-connect/auth'

session4 = requests.Session()

response13 = session4.get(url8, headers=headers3)
print(response13)
print(response13.text)
print(response13.json())



url9 = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/ticket'

headers4 = {
    'Authorization': f'Bearer {token}'
}

session5 = requests.Session()


response14 = session4.get(url9, headers=headers4)
print(response14)
print(response14.text)



