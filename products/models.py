from django.db import models
from django.utils.translation import ugettext_lazy as _

from products.validators import validate_file_extension


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('product name'))
    price = models.PositiveIntegerField(default=0, db_index=True, verbose_name=_('price'))
    taxable = models.BooleanField(default=True, help_text=_('is this product taxable'), verbose_name=_('taxable'))
    image = models.ImageField(verbose_name=_('image'))
    catalog = models.FileField(validators=[validate_file_extension], verbose_name=_('catalog'))
    technical_features = models.TextField(verbose_name=_('technical features'))
    usable_for_organization_product = models.ManyToManyField('OrganizationProduct',
                                                             verbose_name=_('usable for organization product'))

    def __str__(self):
        return self.name


class OrganizationProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name of product that create by some organization'))
    slug = models.SlugField(max_length=20, unique=True, verbose_name=_('slug'))

    def __str__(self):
        return self.name
