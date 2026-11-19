from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.CharField(source="room_type.name")

    class Meta:
        model = Room
        fields = ["id", "number", "floor", "room_type", "housekeeping_status"]
