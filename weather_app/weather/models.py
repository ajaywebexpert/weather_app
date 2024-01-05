# weather/models.py

from django.db import models

class WeatherSearch(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    conditions = models.CharField(max_length=100)
    forecast = models.TextField()
