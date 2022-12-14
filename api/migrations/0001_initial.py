# Generated by Django 4.1.4 on 2022-12-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "headline",
                    models.CharField(default="Enter headline here", max_length=200),
                ),
                (
                    "byline",
                    models.CharField(default="write author name here", max_length=100),
                ),
                (
                    "introduction",
                    models.TextField(default="write intro here", max_length=1500),
                ),
                (
                    "body",
                    models.TextField(
                        default="this is the body of your article", max_length=1500
                    ),
                ),
                (
                    "conclusion",
                    models.TextField(default="conclude your article", max_length=1500),
                ),
            ],
        ),
    ]
