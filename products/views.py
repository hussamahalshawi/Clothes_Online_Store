from django.db.models import  Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView , CreateView , UpdateView , DeleteView, DetailView)
import requests
from .models import Product , Feedback, Category
from .forms import CommentForm
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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

def blog_detail(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    recently_viewed_products = None
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
    if 'recently_viewed' in request.session:
        if pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(pk)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, pk)
        if len(request.session['recently_viewed']) > 4:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [pk]

    request.session.modified = True
    context = {
        "product": product,
        "comments": comments,
        "form": form,
        'recently_viewed_products': recently_viewed_products,
    }
    return render(request, "products/detail.html", context)
def blog_detail_customer(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    recently_viewed_products = None
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
    if 'recently_viewed' in request.session:
        if pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(pk)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, pk)
        if len(request.session['recently_viewed']) > 4:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [pk]

    request.session.modified = True
    context = {
        "product": product,
        "comments": comments,
        "form": form,
        'recently_viewed_products': recently_viewed_products,
    }
    return render(request, "Customer/detail_customer.html", context)
def blog_detail_seller(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm()
    recently_viewed_products = None
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
    if 'recently_viewed' in request.session:
        if pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(pk)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, pk)
        if len(request.session['recently_viewed']) > 4:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [pk]

    request.session.modified = True
    context = {
        "product": product,
        "comments": comments,
        "form": form,
        'recently_viewed_products': recently_viewed_products,
    }
    return render(request, "seller/detail_seller.html", context)
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
    template_name = "seller/add_products.html"
    success_url = reverse_lazy("dashboard_seller")


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
        product = Product.objects.create(
            user = user , name = name , picture = picture , price = price ,
              DiscountPrice=DiscountPrice, Cost = Cost, sizes = sizes ,
                colors = colors, description = description)
        product.save()
        for i in categories:
            product.categories.add(i)
        return redirect("/dashboard_seller")
    return render(request, "seller/add_products.html")


class Productsupdateview (ProductsCreateView,LoginRequiredMixin, UpdateView):
    login_url='/seller_login'
    template_name = "seller/update_products.html"
    success_url = reverse_lazy("products-detail-seller")




@login_required(login_url='/seller_login')
def edit_product(request, pk):
    product = Product.objects.get(id = pk)
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
        product.user = user
        product.name = name
        product.picture = picture
        product.price = price
        product.DiscountPrice = DiscountPrice
        product.Cost = Cost
        product.sizes = sizes
        product.colors = colors
        product.description = description
        # product.categories = categories
        product.save()
        for i in categories:
            product.categories.add(i)
        alert = True
        return redirect('products-detail-seller',pk=pk)
    return render(request, "seller/update_products.html",{'products':product})


def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        user = request.user
        product = Product(
            user = user,
            name = item['title'],
            picture = item['image'],
            price = item['price'],
            sizes = ['s','m','l','xl','xxl'],
            colors = ['bk','w','g','r','bu'],
            description = item['description'],
            
        )
        product.save()
        product.categories.add(1)

    return redirect("/dashboard")


# any one can add product to cart, no need of signin

@login_required(login_url='/Customer_login')
def add_to_cart_view_customer(request,pk):
    products=models.Product.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1
    response = redirect('dashboard_customer')

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    product=models.Product.objects.get(id=pk)
    messages.info(request, product.name + ' added to cart successfully!')

    return response



# for checkout of cart
@login_required(login_url='/Customer_login')
def cart_view_customer(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'Customer/cart_customer.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})


def remove_from_cart_view(request,pk):
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = redirect('cart_customer')
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "seller/prduct_confirm_delete.html"
    success_url = reverse_lazy("dashboard_seller")