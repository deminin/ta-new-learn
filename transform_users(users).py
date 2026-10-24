result = []

users_from_api = [
    {"first_name": "John", "last_name": "Doe", "age": 30},
    {"first_name": "Jane", "last_name": "Smith", "age": 25}
]

for raw_user in users_from_api:
    transformed_user = transform_user(raw_user)
    print(transformed_user)

fruits = []
fruits.append("apple")


result = transform_users(users_from_api)
print(result)