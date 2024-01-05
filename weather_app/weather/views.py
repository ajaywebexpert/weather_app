from django.shortcuts import render
from .models import WeatherSearch
from .forms import CitySearchForm
import requests
import json

def search_weather(request):
    if request.method == 'POST':
        form = CitySearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'your_accuweather_api_key'
            url = f'http://dataservice.accuweather.com/locations/v1/cities/search?q={city}&apikey={api_key}'
            
            # Perform API request to get city details
            response = requests.get(url)
            city_data = json.loads(response.content)
            
            # Extract relevant information from the response
            city_key = city_data[0]['Key']
            city_name = city_data[0]['LocalizedName']
            
            # Use the city key to get current conditions
            url = f'http://dataservice.accuweather.com/currentconditions/v1/{city_key}?apikey={api_key}'
            response = requests.get(url)
            weather_data = json.loads(response.content)[0]

            # Save search history in the database
            WeatherSearch.objects.create(
                city=city_name,
                temperature=weather_data['Temperature']['Metric']['Value'],
                conditions=weather_data['WeatherText'],
                forecast=weather_data['IconPhrase']
            )

            return render(request, 'result.html', {'weather_data': weather_data})
    else:
        form = CitySearchForm()

    return render(request, 'index.html', {'form': form})

def search_history(request):
    history = WeatherSearch.objects.all()
    return render(request, 'history.html', {'history': history})
