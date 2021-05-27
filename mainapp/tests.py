from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class HomeTest(TestCase):
    def test_homepage_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)