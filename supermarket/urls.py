
from django.urls import path
from supermarket.views import home_page,signUpUser,home1,productdetails,Register
from django.urls import path
urlpatterns = [
  
    path("",Register,name='register'),
    path('home',home_page,name='home'),
    path('login',signUpUser,name='signip'),
    path('home1',home1,name='home1'),
    path('productsD',productdetails,name='productsD'),
    
]
