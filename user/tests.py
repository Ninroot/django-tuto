from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test import Client


class UserAuthTests(TestCase):
    def test_connexion_user(self):
        # Every test needs access to the request factory.
        c = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='gaspard', password='top_secret')
        response = c.post('/user/login/', {'username': 'gaspard', 'password': 'top_secret'})
        self.assertEqual(response.status_code, 302)

    def test_creation_user_from_form(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        c = Client()
        response = c.post('/user/signup/', {'username': 'gaspard', 'password1': 'smith', 'password2': 'smith'})
        self.assertEqual(response.status_code, 200)