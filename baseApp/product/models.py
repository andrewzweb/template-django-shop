from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='product', blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.title)

