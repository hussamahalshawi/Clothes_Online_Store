from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)

admin.site.register(customuser)
class ProfileInline(admin.StackedInline):
    model = customuser
class CustomUser(admin.ModelAdmin):
    model = User
    fields = ['email',"username",'first_name','last_name','password']
    inlines = [ProfileInline]
# admin.site.unregister(User)
# admin.site.register(User, CustomUser)
