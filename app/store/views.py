from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StoreSerializer, CitySerializer, CitySerializer2
from .models import Store, Street, City


class StoreView(APIView):

    def get(self, request, *args,):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})

class TestCityView(APIView):

    def get(self, request, pk=None):
        if pk:
            city = City.objects.filter(pk=pk).all()
        else:
            city = City.objects.all().prefetch_related('city_street')
        serializer = CitySerializer2(city, many=True)
        return Response({'city': serializer.data})



class CityView(APIView):

    def get(self, request, pk=None):
        if pk:
            city = City.objects.filter(pk=pk).all()
        else:
            city = City.objects.all().prefetch_related('city_street')
        serializer = CitySerializer(city, many=True)
        return Response({'city': serializer.data})



class StreetView(APIView):
    def get(self, request):
        street = Street.objects.all().prefetch_related('city')
        serializer = CitySerializer2(street, many=True)
        return Response({'streets': serializer.data})


# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
