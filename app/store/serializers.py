from rest_framework import serializers

from .models import Store, Street


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
    city = CitySerializer(many=True, read_only=True)
    street = OnlyStreetNameSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('title', 'city', 'street', 'house', 'time_to_open', 'time_to_close')

    def create(self, validated_data):
        return Store.objects.create(
            title=validated_data['title'],
            city=validated_data['city'],
            street=validated_data['street'],
            house=validated_data['house'],
            time_to_open=validated_data['time_to_open'],
            time_to_close=validated_data['time_to_close']
        )
