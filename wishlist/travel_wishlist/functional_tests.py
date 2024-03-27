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

class AddPlacesTest(LiveServerTestCase):
    # FIXME - This one doesn't quite work right.   StackTrace: 
    #   File "[...]/functional_tests.py", line 43, in test_add_new_place
    #     input_name = self.selenium.find_element_by_id('name')
    #                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'



    fixtures = ['test_places']# stuff that already exists in the test

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_new_place(self):

        self.selenium.get(self.live_server_url)
        input_name = self.selenium.find_element_by_id('name')
        input_name.send_keys('Denver')

        add_button = self.selenium.find_element_by_id('add-new-place')
        add_button.click()

        denver = self.selenium.find_element_by_id('place-name-5')

        self.assertEqual('Denver', denver.text)
        self.assertEqual('New York', denver.text)
        self.assertEqual('Tokyo', denver.text)