from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from products.models import Product, OrganizationProduct
from .validators import phone_validator


class Organization(models.Model):
    province = models.CharField(max_length=20, verbose_name=_('province'))
    name = models.CharField(max_length=50, verbose_name=_('province name'))
    organization_phone = models.CharField(max_length=15, verbose_name=_('organization phone'))
    number_of_workers = models.PositiveIntegerField(verbose_name=_('number of workers'))
    products = models.ManyToManyField('products.OrganizationProduct', verbose_name=_('products'))
    owner_of_organization = models.CharField(max_length=30, verbose_name=_('owner of organization'))
    owner_phone = models.CharField(max_length=15, validators=[phone_validator], verbose_name=_('owner phone'))
    owner_email = models.EmailField(verbose_name=_('owner email'))
    submit_date = models.DateField(auto_now_add=True, verbose_name=_('submit date'))
    submit_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('submit user'))

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
