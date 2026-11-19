from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer


@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "rooms": Room.objects.count()})


class RoomList(ListAPIView):
    queryset = Room.objects.select_related("room_type").order_by("number")
    serializer_class = RoomSerializer
