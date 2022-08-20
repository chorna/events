from rest_framework import serializers

from event.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = 'client', 'event'


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance