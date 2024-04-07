from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm): # Creating new objects here, as far as I understand... 
    class Meta:
        model = Place
        fields = ('name', 'visited')

class DateInput(forms.DateInput): 
    input_type='date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }