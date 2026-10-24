def transform_user(user):
    first = user["first_name"]
    last = user["last_name"]
    user_name = first + " " + last
    new_user = {"full_name": user_name, "age": user["age"]}
    result = []
    for raw_user in user:
        transformed_user = transform_user(raw_user)
        result.append(transformed_user)
    return result

users_from_api = [
    {"first_name": "John", "last_name": "Doe", "age": 30},
    {"first_name": "Jane", "last_name": "Smith", "age": 25}
]

# result = []
# for raw_user in users_from_api:
#     transformed_user = transform_user(raw_user)
#     result.append(transformed_user)
print(transform_users)

