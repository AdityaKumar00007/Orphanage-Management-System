from django.test import TestCase, Client
from django.urls import reverse
from .models import Child, Donation
from datetime import date
from django.contrib.auth.models import User

class ChildModelTest(TestCase):
    def test_child_creation(self):
        child = Child.objects.create(
            name="Test Child",
            age=5,
            gender="Male",
            date_of_birth=date(2018, 1, 1),
            date_of_admission=date(2023, 1, 1)
        )
        self.assertEqual(child.name, "Test Child")
        self.assertEqual(child.is_adopted, False)

class DonationModelTest(TestCase):
    def test_donation_creation(self):
        donation = Donation.objects.create(
            donor_name="Test Donor",
            donation_type="money",
            amount=1000,
            email="test@example.com"
        )
        self.assertEqual(donation.donor_name, "Test Donor")
        self.assertEqual(donation.amount, 1000)

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.child = Child.objects.create(
            name="Test Child",
            age=5,
            gender="Male",
            date_of_birth=date(2018, 1, 1),
            date_of_admission=date(2023, 1, 1)
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_adoption_page(self):
        response = self.client.get(reverse('adoption_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adoption_page.html')

    def test_donation_form(self):
        response = self.client.get(reverse('donate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate.html')

    def test_adopt_child_requires_login(self):
        # Test that adoption requires login
        response = self.client.get(reverse('adopt_child', args=[self.child.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

        # Login and try again
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('adopt_child', args=[self.child.id]))
        self.assertEqual(response.status_code, 200)
