from django.db import models

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200, default='Enter headline here')
    byline = models.CharField(max_length=100, default='write author name here')
    # image = models.ImageField(max_length = 254)
    introduction = models.TextField(max_length=1500, default='write intro here')
    body = models.TextField(max_length=1500, default='this is the body of your article')
    conclusion = models.TextField(max_length=1500, default='conclude your article')

    def __str__(self):
        return self.headline

# from api.models import Article
# a = Article(headline='gaida', byline='by anuj', introduction='gaida came', body='gaida aatanka', conclusion='gaida scary')
# a.save()