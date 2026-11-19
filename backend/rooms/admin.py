from django.contrib import admin

from .models import Room, RoomType

admin.site.register(RoomType)
admin.site.register(Room)
