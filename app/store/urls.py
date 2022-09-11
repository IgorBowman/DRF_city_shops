from django.urls import path
from .views import CityView, AllStreetsCity, Shop

urlpatterns = [
    path('city/', CityView.as_view()),
    path('city/street/', AllStreetsCity.as_view()),
    path('shop/', Shop.as_view()),

]
