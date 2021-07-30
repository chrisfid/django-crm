from django.test import TestCase
from django.shortcuts import resolve_url
from django.urls import reverse

# Create your tests here.


class LandingPageTest(TestCase):
    def test_grt(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')
