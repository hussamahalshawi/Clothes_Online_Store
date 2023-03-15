from django.urls import path
from . import views

urlpatterns = [  
    path("dashboard/",views.Productslistview.as_view(),name="products-list"),
    # path('load/', views.load_products),
    path("dashboard_seller/",views.sellerlistview.as_view(),name="dashboard_seller"),
    path("dashboard_customer/",views.customerlistview.as_view(),name="dashboard_customer"),
    path("add/",views.create_product,name="products-create"),
    path("detail_seller/<int:pk>",views.blog_detail_seller,name = "products-detail-seller"), 
    path("detail_customer/<int:pk>",views.blog_detail_customer,name = "products-detail-customer"), 
    path("detail/<int:pk>",views.blog_detail,name = "products-detail"),
    path("update/<int:pk>",views.edit_product,name = "products-update"),  
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("category/seller/<category>/", views.blog_category_seller, name="blog_category_seller"),
    path("category/customer/<category>/", views.blog_category_Customer, name="blog_category_Customer"),
    path('add-to-cart_customer/<int:pk>/', views.add_to_cart_view_customer,name='add-to-cart_customer'),
    path('cart_customer/', views.cart_view_customer,name='cart_customer'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart_view,name='remove-from-cart'),
    path("Delete/product/<int:pk>",views.ProductDeleteView.as_view(),name="product-Delete"),
]