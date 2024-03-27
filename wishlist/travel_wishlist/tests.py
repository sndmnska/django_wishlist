from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestHomePage(TestCase):

    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list') # looks at the front end of the path 'place_list' entry in urls.py. The url is '', so this returns that url path of ''
        response = self.client.get(home_page_url)
        self.assertTemplateUsed('travel_wishlist/wishlist.html')
        self.assertContains(response, "You have no places in your wishlist")