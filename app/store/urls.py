from django.urls import path
from .views import StoreView

urlpatterns = [
    path('city/', StoreView.as_view()),
]
