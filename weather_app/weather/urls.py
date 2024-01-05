# weather/urls.py

from django.urls import path
from .views import search_weather, search_history

urlpatterns = [
    path('search/', search_weather, name='search_weather'),
    path('history/', search_history, name='search_history'),
]
