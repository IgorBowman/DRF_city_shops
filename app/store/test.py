import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .models import Store, Street, City
from .serializers import StorePostSerializer


class TestStoreApiTestCase(APITestCase):

    def setUp(self):
        self.city1 = City.objects.create(title='Test city1')
        self.street1 = Street.objects.create(city=self.city1, title='test street1')
        self.store_1 = Store.objects.create(
            title='Test store 1',
            city=self.city1,
            street=self.street1,
            house=99,
            time_to_open='10:00:00',
            time_to_close='20:00:00'
        )
        self.city2 = City.objects.create(title='Test city2')
        self.street2 = Street.objects.create(city=self.city2, title='test street2')
        self.store_2 = Store.objects.create(
            title='Test store 2',
            city=self.city2,
            street=self.street2,
            house=99,
            time_to_open='10:00:00',
            time_to_close='20:00:00'
        )
        self.city3 = City.objects.create(title='Test city3')
        self.street3 = Street.objects.create(city=self.city3, title='test street3')
        self.store_3 = Store.objects.create(
            title='Test store 3',
            city=self.city3,
            street=self.street3,
            house=99,
            time_to_open='10:00:00',
            time_to_close='20:00:00'
        )

    def test_get_all_shops(self):
        response = self.client.get(reverse('link_for_test'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, Store.objects.all().count())

    def test_post_method(self):
        data = {
            'title': 'TEST STORE',
            'city': 'CITY',
            'street': 'STREET',
            'house': 1,
            'time_to_open': '10:00:00',
            'time_to_close': '20:00:00'
        }
        json_data = json.dumps(data)
        response = self.client.post(reverse('link_for_test'), data=json_data)
        serializer_data = StorePostSerializer(instance=data).data
        print(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
