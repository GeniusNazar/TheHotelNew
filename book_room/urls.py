from django.urls import path
from book_room import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms-list/", views.room_list, name="rooms-list"),
    path("book-room/", views.book_room, name="book-room"),
    path("booking-details/<int:pk>/", views.booking_details, name="booking-details"),
]