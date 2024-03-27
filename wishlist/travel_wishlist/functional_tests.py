from selenium.webdriver.firefox.webdriver import WebDriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

# This is utilizing selenium, an admittedly complicated automation tool for django testing. 

    #These remind me very much of oop in Android kotlin.  Setup and teardown is required for selenium. 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist', self.selenium.title)
