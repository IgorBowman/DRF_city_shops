from rest_framework import serializers

from .models import Store, Street, City


class CitySerializer(serializers.ModelSerializer):
    """Get all Cities"""

    class Meta:
        model = Street
        fields = ('title',)


class CityStreetSerializer(serializers.ModelSerializer):
    """Get all streets by City"""

    city = CitySerializer()

    class Meta:
        model = Street
        fields = ('city', 'title',)


class OnlyStreetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('title',)


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = OnlyStreetNameSerializer()

    class Meta:
        model = Store
        fields = ('title', 'city', 'street', 'house', 'time_to_open', 'time_to_close')
