from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category

def home(request):
    return render(request, 'home.html',{'logged_in': True if request.user.is_authenticated else False,}) 
def food(request):
    cat=get_object_or_404(Category,slug='food')
    cat1=get_object_or_404(Category,slug='food1')
    cat2=get_object_or_404(Category,slug='food2')
    cat3=get_object_or_404(Category,slug='food3')
    product=cat.product_set.filter(is_available=True)
    product1=cat1.product_set.filter(is_available=True)
    product2=cat2.product_set.filter(is_available=True)
    product3=cat3.product_set.filter(is_available=True)





    return render(request, 'food.html',{'food':product,'food1':product1,'food2':product2,'food3':product3,'logged_in': True if request.user.is_authenticated else False,})

def fashion(request):
    return render(request, 'fashion.html',{'logged_in': True if request.user.is_authenticated else False,})
def craft(request):
    return render(request, 'craft.html',{'logged_in': True if request.user.is_authenticated else False,})
def about(request):
    return render(request, 'about.html',{'logged_in': True if request.user.is_authenticated else False,})

# Create your views here.
