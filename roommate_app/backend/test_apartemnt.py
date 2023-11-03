from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Apartment


class ApartmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass'
        )
        self.apartment = Apartment.objects.create_apartment(
            user=self.user, name='Test Apartment', location='Test Location'
        )

    def test_apartment_str(self):
        self.assertEqual(str(self.apartment), 'Test Apartment')

    def test_apartment_user(self):
        self.assertEqual(self.apartment.user, self.user)

    def test_apartment_name(self):
        self.assertEqual(self.apartment.name, 'Test Apartment')

    def test_apartment_location(self):
        self.assertEqual(self.apartment.location, 'Test Location')