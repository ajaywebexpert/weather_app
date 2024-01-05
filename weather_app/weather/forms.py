# weather/forms.py

from django import forms

class CitySearchForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
