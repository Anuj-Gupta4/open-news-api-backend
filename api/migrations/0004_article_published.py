# Generated by Django 4.1.4 on 2022-12-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_article_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="published",
            field=models.BooleanField(default=False),
        ),
    ]