from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64)
    article = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    days = models.IntegerField()

