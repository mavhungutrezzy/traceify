# Generated by Django 4.1.1 on 2022-09-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("notes", models.TextField(blank=True, null=True)),
                ("location", models.CharField(max_length=255)),
                ("logo", models.CharField(max_length=255)),
                ("date_applied", models.CharField(max_length=255)),
            ],
        ),
    ]
