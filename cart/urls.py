from django.urls import path
from .views import cart, AddToCartView, DecreaseCartItemView


urlpatterns=[

    path('cart/',cart,name='cart' ),  
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'), 
]