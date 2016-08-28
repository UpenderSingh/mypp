from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)


class Product(models.Model): 
    name = models.CharField(max_length = 300)
    slug = models.SlugField(max_length = 150)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'product_photo', blank = True)
    manufacturer = models.CharField(max_length = 300, blank=True)
    price_in_dollars = models.DecimalField(max_digits = 6, decimal_places = 2)

class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)
