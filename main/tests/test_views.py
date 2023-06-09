from django.test import TestCase
from main import forms
# Create your tests here.
class TestPage(TestCase):
    def test_home_page(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'Book Worms')

    def test_about_page(self):
        response=self.client.get("/about_us/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'main/about_us.html')
        self.assertContains(response,'Book Worms')

    def test_contact_us_page(self):
        response=self.client.get("/contact_us/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'main/contact_form.html')
        self.assertContains(response,'Book Worms')
        self.assertIsInstance(
            response.context["form"],forms.ContactForm
        )