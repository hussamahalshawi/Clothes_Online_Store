from django.urls import path
from . import views

urlpatterns = [  
    path("seller_login/", views.seller_login, name="seller_login"),
    path("Customer_login/", views.Customer_login, name="Customer_login"),
    path("user_registration/", views.user_registration, name="user_registration"),
    path("change_password_seller/", views.change_password_seller, name="change_password_seller"),
    path("change_password_customer/", views.change_password_customer, name="change_password_customer"),
    path("logout/", views.Logout, name="logout"),
    path("acount/", views.profile_seller, name="acount_seller"),
    path("acount/", views.profile_customer, name="acount_customer"),
    path("edit_profile_seller/", views.edit_profile_seller, name="edit_profile_seller"),
    path("edit_profile_customer/", views.edit_profile_customer, name="edit_profile_cuustomer"),
]