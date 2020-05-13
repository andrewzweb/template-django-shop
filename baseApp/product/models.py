from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    image = models.ImageField(upload_to='product', blank=True, null=True)
    title = models.CharField(max_length=200, default='', blank=False, unique=True)
    price = models.DecimalField(default=None, max_digits=5, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(default='', blank=True)
    
    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Product, self).save(*args, **kwargs)
