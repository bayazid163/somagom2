from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from shop.models import Product



def cart(request):


    if not request.user.is_authenticated:
        return redirect('login')
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    
    return render(request, 'cart.html', {
        'cart': cart, 
        'items': items,
        'logged_in': True if request.user.is_authenticated else False,

    })


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product,id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        cart_item.quantity += 1
        cart_item.save()
        total_items = cart.items.count()
        return Response({"message": "Item added/increased", "quantity": cart_item.quantity,"total_items": total_items,})

class DecreaseCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        cart = get_object_or_404(Cart,user=request.user)
        product = get_object_or_404(Product,id=product_id)
        cart_item = CartItem.objects.get(cart=cart, product=product)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            message= "Quantity decreased"
        else:
            cart_item.delete()
            return Response({"message": "Item removed from cart"})
        
        return Response({
            "message": message,
            "product_name": product.product_name,
            "quantity": cart_item.quantity,
            "subtotal": cart_item.subtotal,
            "cart_total": cart.total_price})




# Create your views here.
