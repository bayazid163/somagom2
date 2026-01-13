from django.urls import path
from .views import registration
from .views import login


urlpatterns=[

    path('registration/',registration,name='registration' ),
    path('login/',login,name='login' ),
]
