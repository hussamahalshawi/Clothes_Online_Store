from django.db.models import  Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView , CreateView , UpdateView , DeleteView, DetailView)
from .models import Product , Feedback
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Productslistview(ListView):
    model = Product
    template_name = "dashboard.html"
    def get_queryset(self):
        if 'q' in self.request.GET:
            queryset = self.request.GET.get('q')
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
    comments = Feedback.objects.filter(products_feed=product)
    context = {
        "product": product,
        "comments": comments,
        "form": form,
    }
    return render(request, "products/detail.html", context)
class sellerlistview(LoginRequiredMixin,ListView):
    login_url='/seller_login'
    model = Product
    template_name = "seller/dashboard_seller.html"
    def get_queryset(self):
        if 'q' in self.request.GET:
            queryset = self.request.GET.get('q')
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
        if 'q' in self.request.GET:
            queryset = self.request.GET.get('q')
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
    return render(request, "products/product_category.html", context)


class ProductsCreateView(LoginRequiredMixin,CreateView) :
    login_url='/seller_login'
    model = Product

    fields = [
        'name',
        'sizes',
        'colors',
        'picture',
        'price',
        'description',
    ] 
    success_url = reverse_lazy("dashboard_seller")
    template_name = "products/products_form.html"

class Productsupdateview (ProductsCreateView,LoginRequiredMixin, UpdateView):
    login_url='/seller_login'
    success_url = reverse_lazy("dashboard_seller")
