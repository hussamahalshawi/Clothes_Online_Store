from django.db.models import  Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView , CreateView , UpdateView , DeleteView, DetailView)
from .models import Product , Feedback, Category
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Productslistview(ListView):
    model = Product
    template_name = "dashboard.html"
    def get_queryset(self):
        if 'query' in self.request.GET:
            queryset = self.request.GET.get('query')
            object_list = Product.objects.filter(
                Q(name__icontains=queryset) or Q(state__icontains=queryset)
            ).order_by('created_at')
        else:
            object_list = Product.objects.all().order_by('created_at')
        return object_list
    paginate_by = 30

# def SearchResultsView(request):
#     if 'q' in request.GET:
#         query = request.GET['q']
#         data = Product.objects.filter(Q(name__icontains=query) or Q(categories__icontains=query))
#     else:
#         data = Product.objects.all().order_by('created_at')
#     context = {
#         'product_list': data
#     }
#     return render(request, 'dashboard.html', context)
def blog_detail(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Feedback(
                name=form.cleaned_data["name"],
                feedback=form.cleaned_data["feedback"],
                products_feed=product
            )
            comment.save()
            return redirect('products-detail',pk=pk)
    comments = Feedback.objects.filter(products_feed=product)
    context = {
        "product": product,
        "comments": comments,
        "form": form,
    }
    return render(request, "products/detail.html", context)
def blog_detail_customer(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Feedback(
                name=form.cleaned_data["name"],
                feedback=form.cleaned_data["feedback"],
                products_feed=product
            )
            comment.save()
            return redirect('products-detail',pk=pk)
    comments = Feedback.objects.filter(products_feed=product)
    context = {
        "product": product,
        "comments": comments,
        "form": form,
    }
    return render(request, "customer/detail.html", context)
def blog_detail_seller(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Feedback(
                name=form.cleaned_data["name"],
                feedback=form.cleaned_data["feedback"],
                products_feed=product
            )
            comment.save()
            return redirect('products-detail',pk=pk)
    comments = Feedback.objects.filter(products_feed=product)
    context = {
        "product": product,
        "comments": comments,
        "form": form,
    }
    return render(request, "seller/detail.html", context)
class sellerlistview(LoginRequiredMixin,ListView):
    login_url='/seller_login'
    model = Product
    template_name = "seller/dashboard_seller.html"
    def get_queryset(self):
        if 'query' in self.request.GET:
            queryset = self.request.GET.get('query')
            object_list = Product.objects.filter(
                Q(name__icontains=queryset) or Q(state__icontains=queryset)
            ).order_by('created_at')
        else:
            object_list = Product.objects.all().order_by('created_at')
        return object_list
    paginate_by = 30
class customerlistview(LoginRequiredMixin,ListView):
    login_url='/Customer_login'
    model = Product
    template_name = "Customer/dashboard_customer.html"
    def get_queryset(self):
        if 'query' in self.request.GET:
            queryset = self.request.GET.get('query')
            object_list = Product.objects.filter(
                Q(name__icontains=queryset) or Q(state__icontains=queryset)
            ).order_by('created_at')
        else:
            object_list = Product.objects.all().order_by('created_at')
        return object_list
    paginate_by = 30



def blog_category(request, category):
    product = Product.objects.filter(categories__name__contains=category
    ).order_by('-created_at'
    )
    print(product)
    context = {
        "category": category,
        "product": product,
    }
    return render(request, "product_category.html", context)

def blog_category_seller(request, category):
    product = Product.objects.filter(categories__name__contains=category
    ).order_by('-created_at'
    )
    print(product)
    context = {
        "category": category,
        "product": product,
    }
    return render(request, "seller/product_category_seller.html", context)

def blog_category_Customer(request, category):
    product = Product.objects.filter(categories__name__contains=category
    ).order_by('-created_at'
    )
    print(product)
    context = {
        "category": category,
        "product": product,
    }
    return render(request, "Customer/product_category_Customer.html", context)


class ProductsCreateView(LoginRequiredMixin,CreateView) :
    login_url='/seller_login'
    model = Product

    fields = [
        'user',
        'name',
        'picture',
        'price',
        'DiscountPrice',
        'Cost',
        'sizes',
        'colors',
        'categories',
        'description',
    ] 
    success_url = reverse_lazy("dashboard_seller")
    template_name = "seller/add_products.html"


@login_required(login_url='/seller_login')
def create_product(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        picture = request.FILES['picture']
        price = request.POST['price']
        DiscountPrice = request.POST['DiscountPrice']
        Cost = request.POST['Cost']
        sizes = request.POST.getlist('sizes')
        colors = request.POST.getlist('colors')
        description = request.POST['description']
        categories = request.POST.getlist('categories')
        print(user,sizes, colors,categories[0] )
        product = Product.objects.create(
            user = user , name = name , picture = picture , price = price ,
              DiscountPrice=DiscountPrice, Cost = Cost, sizes = sizes ,
                colors = colors, description = description)
        product.save()
        for i in categories:
            product.categories.add(i)
        # categories1 = categories[0]
        # categories2 = categories[1]
        # product.categories.add(categories1)
        # product.categories.add(categories2)
        return redirect("/dashboard_seller")
    return render(request, "seller/add_products.html")


class Productsupdateview (ProductsCreateView,LoginRequiredMixin, UpdateView):
    login_url='/seller_login'
    success_url = reverse_lazy("dashboard_seller")

