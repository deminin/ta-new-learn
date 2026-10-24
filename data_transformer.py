# user = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 30
# }
# first = user["first_name"]
# last = user["last_name"]
# full_name = first + " " + last
# print(full_name)
# print(user["age"])


# product = {
#     "brand": "Apple",
#     "model": "iPhone",
#     "version": "15 Pro"
# }
# brand = product["brand"]
# model = product["model"]
# version = product["version"]
# phone_name = brand + " " + model + " " + version
# print(phone_name)


# products = [
#     {"brand": "Apple", "model": "iPhone", "version": "15 Pro"},
#     {"brand": "Samsung", "model": "Galaxy", "version": "S24"},
#     {"brand": "Google", "model": "Pixel", "version": "8"}
# ]
# brand = products[0]["brand"]
# model = products[0]["model"]
# version = products[0]["version"]
# phone_name01 = brand + " " + model + " " + version
# brand = products[1]["brand"]
# model = products[1]["model"]
# version = products[1]["version"]
# phone_name02 = brand + " " + model + " " + version
# brand = products[2]["brand"]
# model = products[2]["model"]
# version = products[2]["version"]
# phone_name03 = brand + " " + model + " " + version
# print(phone_name01)
# print(phone_name02)
# print(phone_name03)


# products = [
#     {"brand": "Apple", "model": "iPhone", "version": "15 Pro"},
#     {"brand": "Samsung", "model": "Galaxy", "version": "S24"},
#     {"brand": "Google", "model": "Pixel", "version": "8"}
# ]
#
# for product in products:
#     brand = product["brand"]
#     model = product["model"]
#     version = product["version"]
#     phone_name = brand + " " + model + " " + version
#     print(phone_name)
#
#
#
# products = [
#     {"brand": "Apple", "model": "iPhone", "version": "15 Pro"},
#     {"brand": "Samsung", "model": "Galaxy", "version": "S24"},
#     {"brand": "Google", "model": "Pixel", "version": "8"}
# ]
#
# # Варіант 1: Цикл для ВСІХ
# print("=== Всі продукти ===")
# for product in products:
#     phone_name = product["brand"] + " " + product["model"]
#     print(phone_name)
#
# # Варіант 2: Конкретна позиція (як раніше!)
# print("\n=== Тільки другий продукт ===")
# specific = products[0]  # Samsung
# phone_name = specific["brand"] + " " + specific["model"]
# print(phone_name)


def make_full_name(product):
    brand = product["brand"]
    model = product["model"]
    version = product["version"]
    full = brand + " " + model + " " + version
    return full

# Тепер використовуємо функцію:
products = [
    {"brand": "Apple", "model": "iPhone", "version": "15 Pro"},
    {"brand": "Samsung", "model": "Galaxy", "version": "S24"}
]

for product in products:
    name = make_full_name(product)
    print(name)