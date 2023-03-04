from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required

from userauth.models import *
# Create your views here.

# def dashboard(request):
#     return render(request, "dashboard.html")


def user_registration(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        USER_type = request.POST['USER_type']
        profile_pic = request.FILES['profile_pic']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "user_registration.html", {'passnotmatch': passnotmatch})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        Customuser = customuser.objects.create(
            user=user, address=address, mobile=mobile, USER_type=USER_type, profile_pic=profile_pic)
        user.save()
        Customuser.save()
        print(USER_type)
        if USER_type == 's':
            return redirect("/seller_login")
        else:
            return redirect("/Customer_login")
    return render(request, "user_registration.html")


def seller_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            dj_login(request, user)
            if request.user.is_superuser or user.customuser.USER_type is not "s":
                return HttpResponse("You are not a seller!!")
            else:
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()
                    return redirect("/dashboard_seller")
                    # return HttpResponse("You're logged in.")
                else:
                    return redirect("/dashboard_seller")
                    # return HttpResponse("Please enable cookies and try again.")

        else:
            alert = True
            return render(request, "seller/seller_login.html", {'alert': alert})
    return render(request, "seller/seller_login.html")


def Customer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            if user.is_superuser:
                return HttpResponse("You are not a Customer!!")
            else:
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()
                    return redirect("/dashboard_customer")
                    # return HttpResponse("You're logged in.")
                else:
                    return redirect("/dashboard_customer")
                    # return HttpResponse("Please enable cookies and try again.")
        else:
            alert = True
            return render(request, "Customer/customer_login.html", {'alert': alert})
    request.session.set_test_cookie()
    return render(request, "Customer/customer_login.html")


def Logout(request):
    logout(request)
    return redirect("/dashboard/")

@login_required(login_url='/seller_login')
def change_password_seller(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "seller/change_password_seller.html", {'alert': alert})
            else:
                currpasswrong = True
                return render(request, "seller/change_password_seller.html", {'currpasswrong': currpasswrong})
        except:
            pass
    return render(request, "seller/change_password_seller.html")

@login_required(login_url='/customer_login')
def change_password_customer(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "Customer/change_password_customer.html", {'alert': alert})
            else:
                currpasswrong = True
                return render(request, "Customer/change_password_customer.html", {'currpasswrong': currpasswrong})
        except:
            pass
    return render(request, "Customer/change_password_customer.html")


@login_required(login_url='/seller_login')
def profile_seller(request):
    return render(request, "seller/profile_seller.html")


@login_required(login_url='/customer_login')
def profile_customer(request):
    return render(request, "Customer/profile_customer.html")


@login_required(login_url='/seller_login')
def edit_profile_seller(request):

    Customuser = customuser.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        profile_pic = request.FILES['profile_pic']
        Customuser.user.email = email
        Customuser.user.username = username
        Customuser.user.first_name = first_name
        Customuser.user.last_name = last_name
        Customuser.address = address
        Customuser.mobile = mobile
        Customuser.profile_pic = profile_pic
        Customuser.user.save()
        Customuser.save()
        alert = True
        return render(request, "seller/profile_seller.html", {'alert': alert})
    return render(request, "seller/edit_profile_seller.html")


@login_required(login_url='/seller_login')
def edit_profile_customer(request):

    Customuser = customuser.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        profile_pic = request.FILES['profile_pic']
        Customuser.user.email = email
        Customuser.user.username = username
        Customuser.user.first_name = first_name
        Customuser.user.last_name = last_name
        Customuser.address = address
        Customuser.mobile = mobile
        Customuser.profile_pic = profile_pic
        Customuser.user.save()
        Customuser.save()
        alert = True
        return render(request, "Customer/profile_customer.html", {'alert': alert})
    return render(request, "Customer/edit_profile_customer.html")
