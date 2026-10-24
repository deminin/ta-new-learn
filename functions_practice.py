def make_full_name(product):
    print("  >> зайшли в функцію, отримали:", product["brand"])
    brand = product["brand"]
    model = product["model"]
    version = product["version"]
    full = brand + " " + model + " " + version
    print("  >> віддаємо назад:", full)
    return full

products = [
    {"brand": "Apple", "model": "iPhone", "version": "15 Pro"},
    {"brand": "Samsung", "model": "Galaxy", "version": "S24"}
]

print("Старт програми")

for product in products:
    print("Викликаємо функцію...")
    name = make_full_name(product)
    print("Отримали в name:", name)
    print("---")