from django.db import models


class Application(models.Model):

    __tablename__ = "applications"

    name = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    status = models.CharField(max_length=50, blank=False, null=False)
    notes = models.TextField(blank=True, default="Add some notes", null=True)
    location = models.CharField(max_length=255, blank=False, null=False)
    logo = models.CharField(max_length=255, blank=False, null=False)
    date_applied = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
