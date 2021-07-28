from django.contrib.auth.models import User
from django.db import models

from products.models import Product, OrganizationProduct
from .validators import phone_validator


class Organization(models.Model):
    province = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    organization_phone = models.CharField(max_length=15)
    number_of_workers = models.PositiveIntegerField()
    products = models.ManyToManyField('products.OrganizationProduct')
    owner_of_organization = models.CharField(max_length=30)
    owner_phone = models.CharField(max_length=15, validators=[phone_validator])
    owner_email = models.EmailField()
    submit_date = models.DateField(auto_now_add=True)
    submit_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_recommended_products(self):
        related_product_list = list()
        for organization_product in self.products.all():
            organization_product_pk = organization_product.pk
            related_product = OrganizationProduct.objects.get(pk=organization_product_pk)
            for product in related_product.product_set.all():
                related_product_list.append(product.name)
        return ', '.join(set(related_product_list))
