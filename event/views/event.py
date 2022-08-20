from rest_framework import generics

from ..serializers.event import EventSerializer
from ..models import Event


class EventCreateAPIView(generics.CreateAPIView):
    serializer_class = EventSerializer


class EventPublicListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(type=Event.PUBLIC_CHOICE)

