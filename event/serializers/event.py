from rest_framework import serializers

from event.models import Event, Room


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        room = data['room']
        capacity = data['capacity']
        room_capacity = room.capacity
        if capacity > room_capacity:
            raise serializers.ValidationError("The capacity must not be greater than room capacity")
        return data