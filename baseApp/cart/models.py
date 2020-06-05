from django.db import models
from product.models import Product

class Cart(models.Model):
    title = models.CharField(max_length=200)
    #count = models.DecimalField()
    def __str__(self):
        return "%s" % (self.title)

    

class CartItem(models.Model):
    title = models.CharField(max_length=200)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField(default=0, blank=False)
    price = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return "%s" % (self.title)

    
    def save(self, *args, **kwargs):
        pass
        
        
