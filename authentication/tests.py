from django.test import TestCase

from .models import User


class UserTestCase(TestCase):
    def setUp(self):

        User.objects.create(
            first_name="Adivhaho",
            last_name="Mavhungu",
            email="mavhungu@gmail.com",
        )

    def user_creation_test(self):
        user = User.objects.get(first_name="Adivhaho")
        self.assertEqual(user.first_name, "Adivhaho")
        self.assertEqual(user.last_name, "Mavhungu")
