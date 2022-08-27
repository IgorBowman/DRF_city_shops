from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StoreSerializer, CitySerializer
from .models import Store, Street, City


class StoreView(APIView):

    def get(self, request, *args,):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})


class CityView(APIView):

    def get(self, request, *args,):
        city = City.objects.all().prefetch_related('city_street')
        # city = City.objects.select_related('city_street').all()
        serializer = CitySerializer(city, many=True)
        return Response({'city': serializer.data})

