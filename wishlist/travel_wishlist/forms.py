from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm): # Creating new objects here, as far as I understand... 
    class Meta:
        model = Place
        fields = ('name', 'visited')