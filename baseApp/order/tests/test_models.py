from django.test import TestCase
from order.models import * 

class OrderModelTest(TestCase):
    ''' test order model '''

    def test_create_order(self):
        ''' test create order '''
        assert Order.objects.count() == 0
        order = Order.objects.create(first_name = 'Jonh')
        assert Order.objects.count() == 1

    def test_create_two_orders(self):
        ''' test create two orders '''

        assert Order.objects.count() == 0
        order = Order.objects.create(first_name = 'Jonh')
        order = Order.objects.create(first_name = 'Jonh')
        assert Order.objects.count() == 2

    def test_after_create_order_paid_false(self):
        ''' test after create order paid false  '''
        
        assert Order.objects.count() == 0
        order = Order.objects.create(first_name = 'Jonh')
        assert order.paid == False
        assert Order.objects.count() == 1

class OrderItemTest(TestCase):
    
    def test_create_order_item(self):
        
        order = Order.objects.create(first_name = 'Jonh')
        product = Product.objects.create(title='prod', price=2)
        price = 2
        item = OrderItem.objects.create(order=order, product=product, price=price)
        
        assert Order.objects.count() == 1
        assert OrderItem.objects.count() == 1
        assert Product.objects.count() == 1

        assert item.order is order
        assert item.product is product
