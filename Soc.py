

def get_user_data(user_id):
    return {"id": user_id, "name":"Moon Light", "age": 18}

def display_user_data(user_data):
    print(f'User ID: {user_data["id"]}')
    print(f'Name: {user_data["name"]}')
    print(f'Age: {user_data["age"]}')

user_data = get_user_data(1)
display_user_data(user_data)

