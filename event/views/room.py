from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from ..serializers.room import RoomSerializer
from ..models import Room


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer



class RoomDestroyAPIView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            event = getattr(obj, 'event')
            return Response(
                data={'message': "You can delete this room because exist an event"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except AttributeError:
            return self.destroy(request, *args, **kwargs)
