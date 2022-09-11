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


class StorePostSerializer(serializers.ModelSerializer):
    """Serializer for POST request"""
    city = CitySerializer()
    street = OnlyStreetNameSerializer()

    class Meta:
        model = Store
        fields = ('title', 'city', 'street', 'house', 'time_to_open', 'time_to_close')

    def create(self, validated_data):
        store_data = validated_data.pop('city', None)
        store_data2 = validated_data.pop('street', None)
        if store_data:
            store_data = Store.objects.get_or_create(**store_data)
            print(f"STORE DATA: {store_data}")
            validated_data['city'] = store_data
        if store_data2:
            store_data2 = Street.objects.get_or_create(**store_data2)
            print(f"STORE DATA: {store_data2}")
            validated_data['street'] = store_data

        return Store.objects.create(**validated_data)
