from django.urls import path
from .views import StoreView, CityView, StreetView, TestCityView

urlpatterns = [
    path('cities/', TestCityView.as_view()),
    path('store/', StoreView.as_view()),
    path('city/', CityView.as_view()),
    path('city/<int:pk>', CityView.as_view()),
    path('street/', StreetView.as_view()),

]
