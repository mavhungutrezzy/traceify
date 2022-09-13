from django.test import TestCase

from .models import Application


class ApplicationTestCase(TestCase):
    def setUp(self):
        Application.objects.create(
            name="Test Name",
            title="Test Title",
            status="Test Status",
            notes="Test Notes",
            location="Test Location",
            logo="Test Logo",
            date_applied="Test Date Applied",
        )

    def test_application(self):
        application = Application.objects.get(name="Test Name")
        self.assertEqual(application.name, "Test Name")
        self.assertEqual(application.title, "Test Title")
        self.assertEqual(application.status, "Test Status")
        self.assertEqual(application.notes, "Test Notes")
        self.assertEqual(application.location, "Test Location")
        self.assertEqual(application.logo, "Test Logo")
        self.assertEqual(application.date_applied, "Test Date Applied")
