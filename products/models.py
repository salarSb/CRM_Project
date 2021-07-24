from django.db import models

from products.validators import validate_file_extension


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0, db_index=True)
    taxable = models.BooleanField(default=True, help_text='is this product taxable')
    catalog = models.FileField(validators=[validate_file_extension])
    technical_features = models.TextField()
    usable_for_organization_product = models.ManyToManyField('OrganizationProduct')

    def __str__(self):
        return self.name


class OrganizationProduct(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
