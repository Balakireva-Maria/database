from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
class Phone(models.Model):

    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.TextField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=30, unique=True)

def __str__(self):
    return self.name

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Phone.filter(slug=slug).order_by('id')
    return slug
