from django.urls import path
from . import views

urlpatterns = [  
    # path("dashboard/",views.SearchResultsView,name="products-list"),
    path("dashboard/",views.Productslistview.as_view(),name="products-list"),
    path("dashboard_seller/",views.sellerlistview.as_view(),name="dashboard_seller"),
    path("dashboard_customer/",views.customerlistview.as_view(),name="dashboard_customer"),
    path("add/",views.ProductsCreateView.as_view(),name="products-create"),
    # path("add/",views.create_product,name="products-create"),
    path("detail/<int:pk>",views.blog_detail,name = "products-detail"),  
    path("update/<int:pk>",views.Productsupdateview.as_view(),name = "products-update"),  
    path("category/<category>/", views.blog_category_seller, name="blog_category_seller"),
    path("category/<category>/", views.blog_category_Customer, name="blog_category_Customer"),

    # path("search/", views.SearchResultsView.as_view(), name="search"),
]