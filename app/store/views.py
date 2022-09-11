from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CitySerializer, CityStreetSerializer, StoreSerializer
from .models import Store, Street, City


class CityView(APIView):
    """Get all cities"""

    def get(self, request):
        city = City.objects.all().prefetch_related('city_street')
        serializer = CitySerializer(city, many=True)
        return Response({'data': serializer.data})


class AllStreetsCity(APIView):
    """Get all streets by city"""

    def get(self, request):
        city = request.GET.get('city')
        streets = Street.objects.filter(city=city)
        serializer = CityStreetSerializer(streets, many=True)
        return Response({'data': serializer.data})


class Shop(APIView):
    """Get shops"""

    def get(self, request):
        city = request.GET.get('city')
        street = request.GET.get('street')
        # open = request.GET.get('open') # 1/0
        if street is not None:
            shops = Store.objects.filter(street=street).all()
        elif city is not None:
            shops = Store.objects.filter(city=city).all()
        elif city and street is not None:
            shops = Store.objects.filter(city=city).filter(street=street).all()
        else:
            shops = Store.objects.all()
        serializer = StoreSerializer(shops, many=True)
        return Response({'data': serializer.data})
