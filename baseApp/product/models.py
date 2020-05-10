from django.db import models


class Product(models.Model):
    title = models.ImageField(upload_to='product')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
