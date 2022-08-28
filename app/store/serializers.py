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


# class CitySerializer(serializers.Serializer):
#
#     # streets = serializers.SlugRelatedField(
#     #     slug_field="street", queryset=Street.objects.all(),
#     #     required=False
#     # )
#     #streets = serializers.ListSerializer(slug_field="street", queryset=Street.objects.all())
#     title = serializers.CharField(max_length=150)
#     cities = StreetSerializer(read_only=True, many=True)
#
#     def create(self, validated_data):
#         return City.objects.create(**validated_data)


class StreetSerializer(serializers.ModelSerializer):
    """Попытка сериализовать Улицу и прибавить магазины если они есть"""
    class Meta:
        model = Street
        fields = ('title',)


class CitySerializer(serializers.ModelSerializer):
    cities = StreetSerializer(read_only=True, many=True)
    class Meta:
        model = Street
        fields = ('title', 'cities',)


class StreetSerializer2(serializers.ModelSerializer):
    """Попытка сериализовать Улицу и прибавить магазины если они есть"""
    city = serializers.CharField()

    class Meta:
        model = Street
        fields = ('title')


class CitySerializer2(serializers.ModelSerializer):
    streets = StreetSerializer(read_only=True, many=True)
    stritt = StreetSerializer2(read_only=True, many=True)

    class Meta:
        model = City
        fields = ('title', 'streets', 'stritt',)
