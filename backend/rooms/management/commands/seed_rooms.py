from django.core.management.base import BaseCommand

from rooms.models import Room, RoomType

# 85 номерів на 5 поверхах, 5 категорій (як у паспорті проєкту)
TYPES = [("Стандарт", 2, 2400), ("Покращений", 2, 2900), ("Сімейний", 4, 3600),
         ("Напівлюкс", 2, 4200), ("Люкс", 2, 5800)]
FLOORS = 5
ROOMS_PER_FLOOR = 17


def type_for(index, types):
    if index <= 8:
        return types[0]
    if index <= 12:
        return types[1]
    if index <= 14:
        return types[2]
    if index <= 16:
        return types[3]
    return types[4]


class Command(BaseCommand):
    help = "Заповнює номерний фонд тестовими даними (85 номерів)"

    def handle(self, *args, **options):
        if Room.objects.exists():
            self.stdout.write("Номери вже є, пропускаю")
            return
        types = [RoomType.objects.get_or_create(name=n, defaults={"capacity": c, "base_price": p})[0]
                 for n, c, p in TYPES]
        for floor in range(1, FLOORS + 1):
            for i in range(1, ROOMS_PER_FLOOR + 1):
                Room.objects.create(number=f"{floor}{i:02d}", floor=floor, room_type=type_for(i, types))
        self.stdout.write(self.style.SUCCESS(f"Створено {Room.objects.count()} номерів"))
