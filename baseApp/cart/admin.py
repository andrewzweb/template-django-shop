from django.contrib import admin
from cart.models import *


class CartInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartInline
    ]

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)

