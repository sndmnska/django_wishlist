from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestHomePage(TestCase):

    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list') # looks at the front end of the path 'place_list' entry in urls.py. The url is '', so this returns that url path of ''
        response = self.client.get(home_page_url)
        self.assertTemplateUsed('travel_wishlist/wishlist.html') # What template was used
        self.assertContains(response, "You have no places in your wishlist") # What dies the 


class TestWishList(TestCase):

    fixtures = ['test_places'] # assumes .json extension

    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed('travel_wishlist/wishlist.html') # Assert correct template
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, "New York")
        self.assertNotContains(response, "San Francisco")
        self.assertNotContains(response, "Moab")

class TestVisitedPage(TestCase):

    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited')) # Reverse this url by it's django name...?
        self.assertTemplateUsed('travel_wishlist/visited.html') 
        self.assertContains(response, 'You have not visited any places yet')

class VisitedList(TestCase):

    fixtures = ['test_places']

    def test_visited_list_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed('travel_wishlist/visited.html') 
        self.assertNotContains(response, 'Tokyo') # It's the opposite results from before!
        self.assertNotContains(response, "New York")  # Using vim totally made this an easy bit of coding. :-)
        self.assertContains(response, "San Francisco")
        self.assertContains(response, "Moab")

class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list') # Using the '' url for both POST and GET requests, remember that
        new_place_data = {'name': 'Tokyo', 'visited': False }

        response = self.client.post(add_place_url, new_place_data, follow=True) # Follow the redirect, since this action is both POST then GET. 

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(1, len(response_places))
        tokyo_from_response = response_places[0]

        tokyo_from_database = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_from_database, tokyo_from_response)

class TestVisitPlace(TestCase):

    fixtures = ['test_places']

    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2, )) # Visit New York -- args is a Tuple here for NY primary key 'pk'
        response = self.client.post(visit_place_url, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        self.assertContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')

        new_york = Place.objects.get(pk=2) # Check that a change was made, 
        self.assertTrue(new_york.visited)

    def test_non_existant_place(self):
        visit_nonexistant_place_url = reverse('place_was_visited', args=(987654321, ))
        response = self.client.post(visit_nonexistant_place_url, follow=True)
        self.assertEqual(404, response.status_code)