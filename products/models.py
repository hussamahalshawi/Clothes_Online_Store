from django.db import models
from django.contrib.auth.models import User
# from django.forms import CharField
from django_mysql.models import ListCharField
from django.db.models.signals import post_save
from django.dispatch import receiver

##########################Category################################
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
##########################Product_model################################
class Product(models.Model):
    user = models.ForeignKey(User, related_name="product", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='photo/', blank=True, null=True)
    price = models.PositiveIntegerField()
    description=models.TextField(verbose_name=("Description"))
    DiscountPrice = models.DecimalField(max_digits=5,blank=True, null=True  , decimal_places=2 , verbose_name=("Discount Price"))
    Cost = models.DecimalField(max_digits=5 ,blank=True, null=True, decimal_places=2 , verbose_name=("Cost"))
    size = [
        ('s','small'),
        ('m','medium'),
        ('l', 'larg'),
        ('xl', 'x_larg'),
        ('xxl', 'xx_larg')
    ]
    sizes = ListCharField(
        base_field=models.CharField(max_length=10, choices=size),
        size=5,
        max_length=(5 * 11),  # 6 * 10 character nominals, plus commas
    )
    color = [
        ('w', 'white'),
        ('g', 'green'),
        ('r', 'red'),
        ('bu', 'blue'),
        ('bk', 'black'),
    ]
    colors = ListCharField(
        base_field=models.CharField(max_length=10, choices=color),
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
    )
    categories = models.ManyToManyField('Category',blank=True, null=True,
     related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.id) + str(self.name)+str(self.picture) \
        +str(self.price)+str(self.description)+str(self.DiscountPrice)+str(self.Cost)+str(self.sizes)+str(self.colors)+str(self.categories)
@receiver(post_save, sender=Category)
def create_Product(sender, instance, created, **kwargs):
    if created:
        categories_Product = Product(category=instance)
        categories_Product.save()
        categories_Product.categories.set([instance.product.id])
        categories_Product.save() 

#############################Feedback_model###################################
class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.TextField()
    date= models.DateTimeField(auto_now_add=True,null=True)
    products_feed = models.ForeignKey('Product', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

