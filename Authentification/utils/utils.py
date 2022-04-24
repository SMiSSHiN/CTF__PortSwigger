import sys

def read_usernames():
    with open('../utils/usernames.txt', 'r') as f:
        USERNAMES = [username[:-1] for username in f.readlines()]

    return USERNAMES

def read_passwords():
    with open('../utils/passwords.txt', 'r') as f:
        PASSWORDS = [password[:-1] for password in f.readlines()]

    return PASSWORDS
