from django.urls import path

from .views.room import RoomCreateAPIView, RoomDestroyAPIView
from .views.event import EventCreateAPIView, EventPublicListAPIView
from .views.book import BookCreateAPIView, BookUpdateAPIView

urlpatterns = [

    path(
        'room/create',
        RoomCreateAPIView.as_view(),
        name='room_create'
    ),
    path(
        'room/delete/<int:pk>',
        RoomDestroyAPIView.as_view(),
        name='room_delete'
    ),

    path(
        'event/create',
        EventCreateAPIView.as_view(),
        name='event_create'
    ),
    path(
        'event/list',
        EventPublicListAPIView.as_view(),
        name='event_list'
    ),

    path(
        'book/create',
        BookCreateAPIView.as_view(),
        name='book_create'
    ),
     path(
        'book/<int:pk>/cancel',
        BookUpdateAPIView.as_view(),
        name='book_cancel'
    ),

]