from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required  # import login require decorator
from django.http import HttpResponseForbidden

@login_required
def place_list(request):
    if request.method == 'POST':
        form =  NewPlaceForm(request.POST) # creating a form from data that's in the request.
        place = form.save(commit=False)  # creating a model object from form || Commmit True (or '()')saves to database. 
        place.user = request.user
        if form.is_valid(): # validation object against DB constraints
            place.save() # saves place to DB
            return redirect('place_list')  # reloads home page

    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # Used to create html
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def about(request):
    author = 'Dan'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })

@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save()
        else: 
            return HttpResponseForbidden()
    return redirect('place_list')

@login_required
def place_details(request, place_pk): # place_pk from url.py
    place = get_object_or_404(Place, pk=place_pk)
    return render(request, 'travel_wishlist/place_detail.html', {'place': place})

@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect(place_list) # Makes a brand new request to the place_list. 
    else:
        return HttpResponseForbidden()