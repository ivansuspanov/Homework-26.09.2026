from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79110000001"),
    Smartphone("Samsung", "Galaxy S24", "+79110000002"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79110000003"),
    Smartphone("Google", "Pixel 8", "+79110000004"),
    Smartphone("Honor", "Magic 6", "+79110000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")