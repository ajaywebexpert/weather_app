from django.contrib import admin
from weather.models import WeatherSearch
# Register your models here.

class WeatherCol(admin.ModelAdmin):
    list_display = ("city","timestamp","temperature","conditions","forecast")

admin.site.register(WeatherSearch,WeatherCol)

