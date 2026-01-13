from django.db import models
from category.models import Category 


class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=500,blank=True)
    price=models.PositiveIntegerField(blank=True)
    images=models.ImageField(upload_to='photos/products')
    quantity=models.CharField(max_length=200,blank=True)
    stock=models.PositiveIntegerField()
    origin=models.CharField(max_length=200,blank=True)
    status=models.CharField(max_length=200,blank=True)  
    authenticity=models.CharField(max_length=200,blank=True)           
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


# Create your models here.
