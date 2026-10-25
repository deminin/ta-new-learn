# browsers = ['Chrome', 'Firefox', 'Edge']
# browsers.append('Safari')
#
# for browser in browsers:
#     print(f"Running tests in {browser}")
# print(f"All {len(browsers)} browsers done")

# print("___________________________________")

users = [
    {"name": "Dmytro", "role": "admin"},
    {"name": "Olena", "role": "tester"},
    {"name": "Taras", "role": "viewer"}
]

for user in users:
    # name = users["name"]
    # role = users["role"]
    # print(f"{users["name"]} is {users["role"]}")
    position = f"{user['name']} is {user['role']}"
    # print(user["name"], ["role"])
    print(position)