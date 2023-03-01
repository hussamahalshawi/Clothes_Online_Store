from django.urls import path
from . import views

urlpatterns = [  
    path("seller_login/", views.seller_login, name="seller_login"),
    path("Customer_login/", views.Customer_login, name="Customer_login"),
    path("user_registration/", views.user_registration, name="user_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("logout/", views.Logout, name="logout"),
]