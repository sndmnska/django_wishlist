from django.urls import path
from . import views

# Notice how these are connected.  
# the first argument is the html tags, and a '' argument could be thought of as the 'homepage'
# second is the connection to views. 
# I think the third argument is a django label, if I'm understanding this right.  This connects the html with the view with the django. I think. 
urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('about', views.about, name='about'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited')
]