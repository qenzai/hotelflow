from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health),
    path("rooms/", views.RoomList.as_view()),
]
