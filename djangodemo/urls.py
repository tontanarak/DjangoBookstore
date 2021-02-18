"""djangodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('Payment/<int:ID>',views.pay),
    path('Payment/Details/<int:ID>',views.paydetials),
    path('ConfirmPayment/',views.confirmpayment),
    path('payment/',views.payment),
    path('Booklist/',views.booklist),
    path('Book/<int:bookID>',views.book),
    path('AddToCart/<int:bookID>/<int:userID>',views.addtocart),
    path('Cart/<int:userID>',views.cart),
    path('DeleteCart/<int:id>/<int:userID>',views.deletecart),
    path('AddPayment/<int:userID>',views.addpayment),
    path('HowToBuy/',views.howtobuy),
    path('Signup/',views.signup),
    path('AddUser/',views.addUser),
    path('Signin/',views.signin),
    path('Login/',views.login),
    path('Logout/',views.logout),

]
