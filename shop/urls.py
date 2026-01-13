from django.urls import path 
from . import views           


urlpatterns=[
    path('',views.home,name=''),
    path('food/',views.food,name='food'),
    path('fashion/',views.fashion,name='fashion'),
    path('craft/',views.craft,name='craft'),
    path('about/',views.about,name='about'),

]