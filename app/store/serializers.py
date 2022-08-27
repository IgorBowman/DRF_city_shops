from rest_framework import serializers

from .models import Store, Street, City


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    city = serializers.CharField()
    street = serializers.CharField()
    house = serializers.CharField()
    time_to_open = serializers.TimeField()
    time_to_close = serializers.TimeField()

    def create(self, validated_data):
        return Store.objects.create(**validated_data)


class CitySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return City.objects.create(**validated_data)