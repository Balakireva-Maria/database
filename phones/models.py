from django.db import models


class Phone(models.Model):

    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.TextField()
    slug = models.BooleanField()

def __str__(self):
    return