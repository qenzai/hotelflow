from django.db import models


class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveSmallIntegerField(default=2)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Room(models.Model):
    class Housekeeping(models.TextChoices):
        DIRTY = "dirty"
        IN_PROGRESS = "in_progress"
        CLEAN = "clean"
        INSPECTED = "inspected"
        OUT_OF_ORDER = "out_of_order"

    number = models.CharField(max_length=10, unique=True)
    floor = models.PositiveSmallIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, related_name="rooms")
    housekeeping_status = models.CharField(
        max_length=20, choices=Housekeeping.choices, default=Housekeeping.CLEAN)

    def __str__(self):
        return self.number
