import re


def is_username_valid(username: str) -> bool:
    return 3 < len(username) < 20

def is_password_strong(password: str) -> bool:
    return (
        len(password) >= 8
        and any(char.isupper()for char in password)
        and any(char.isdigit()for char in password)
    )

users = []
def add_user_to_database(username: str, password: str):

    users.append({"username": username, "password": password})
    print(f'User {username} has been successfully added to the database.')
    return users

def user_register(username: str, password: str):
    if not is_username_valid(username):
        print('Invalid username. Username must be between 4 and 19 characters.')
        return
    if not is_password_strong(password):
        print('Password is too weak. Must be at least 8 characters, with a number and an uppercase letter.')
        return

    users =add_user_to_database(username,password)
    return users

user_register('Jane Poem Smith','passwordisGreat12*')
