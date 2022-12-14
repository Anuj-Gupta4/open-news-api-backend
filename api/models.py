from django.db import models

# Create your models here.
class Article(models.Model):
    tag_choice = [
        ('NATIONAL', 'National'),
        ('FASHION', 'Fashion'),
        ('SPORTS', 'Sports'),
        ('POLITICS', 'Politics'),
        ('FINANCE', 'Finance'),
        ('OTHERS', 'Others')
    ]
    headline = models.CharField(max_length=200, default='Enter headline here')
    byline = models.CharField(max_length=100, default='write author name here')
    image = models.ImageField(upload_to="my_picture", blank=True)
    introduction = models.TextField(
        max_length=1500, default='write intro here')
    body = models.TextField(
        max_length=1500, default='this is the body of your article')
    conclusion = models.TextField(
        max_length=1500, default='conclude your article')
    published = models.BooleanField(default=False)
    tags = models.CharField(
        max_length=10, choices=tag_choice, default='OTHERS',)

    def __str__(self):
        return self.headline

# from api.models import Article
# a = Article(headline='gaida', byline='by anuj', introduction='gaida came', body='gaida aatanka', conclusion='gaida scary')
# a.save()
