from address import Address
from mailing import Mailing

from_address = Address("610000", "Киров", "Ленина", "10", "5")
to_address = Address("613800", "Сосновка", "Мира", "25", "12")

mailing = Mailing(to_address, from_address, 350, "EA123456789RU")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.building} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)