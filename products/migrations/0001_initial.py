# Generated by Django 4.1.4 on 2023-03-01 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("picture", models.ImageField(blank=True, upload_to="photo/")),
                ("price", models.PositiveIntegerField()),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "DiscountPrice",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Discount Price"
                    ),
                ),
                (
                    "Cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Cost"
                    ),
                ),
                (
                    "sizes",
                    django_mysql.models.ListCharField(
                        models.CharField(
                            choices=[
                                ("s", "small"),
                                ("m", "medium"),
                                ("l", "larg"),
                                ("xl", "x_larg"),
                                ("xxl", "xx_larg"),
                            ],
                            max_length=10,
                        ),
                        max_length=55,
                        size=5,
                    ),
                ),
                (
                    "colors",
                    django_mysql.models.ListCharField(
                        models.CharField(
                            choices=[
                                ("w", "white"),
                                ("g", "green"),
                                ("y", "yellow"),
                                ("o", "orange"),
                                ("bu", "blue"),
                                ("bk", "black"),
                            ],
                            max_length=10,
                        ),
                        max_length=66,
                        size=6,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="product",
                        to="products.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "PRDIImage",
                    models.ImageField(upload_to="prodcut/", verbose_name="Image"),
                ),
                (
                    "PRDIProduct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="Product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("feedback", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "products_feed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]