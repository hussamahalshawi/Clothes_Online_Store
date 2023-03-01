from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    profile_pic= models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USER_TYPE = (
        ('s', 'seller'),
        ('c', 'customer'),
    )
    USER_type = models.CharField(
        max_length=20,
        choices=USER_TYPE
    )
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return str(self.user.id) + str(self.user.first_name)+str(self.user.last_name) +str(self.address)+str(self.USER_type)