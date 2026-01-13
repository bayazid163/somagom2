from django.db import models
from shop.models import Product
from django.conf import settings    


class Cart(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.email}"
    
    @property 
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} X {self.product.product_name}"
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity
