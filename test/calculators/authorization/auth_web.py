import requests
import json
from test.calculators.authorization.src import headers
import urllib3


def auth():
    url = "https://club.gteh.pro/backend/login"
    header = headers()
    payload = json.dumps({
        "email": f'unicomclient3@gteh.pro',
        "password": f'unicomclient3@gteh.pro'
    })

    response = requests.post(url, headers=header, json=payload, verify=False)
    print(f"Статус ответа: {response.status_code}")
    print(f"Тело ответа: {response.text}")

    if response.status_code == 200:
        data = response.json()
        token = data.get('data', {}).get('token')
        if token:
            print("Успешная авторизация")
            return token
    else:
        raise Exception(f"Authentication failed with status code {response.status_code}")

    # data = session.post(url, headers=header, data=payload, verify=False)
    # if data.status_code != 200:
    #     raise Exception(f"Authentication failed with status code {data.status_code}")
    #
    # data_loads = json.loads(data.text)
    # token = data_loads.get('data').get('token')
    # if not token:
    #     raise Exception("Token not found in the response")
    #
    # header = headers.headers_token(token)
    # return header


try:
    urllib3.disable_warnings()
    auth_headers = auth()
    print("Заголовки с токеном:", auth_headers)
except Exception as e:
    print("Ошибка авторизации:", str(e))
