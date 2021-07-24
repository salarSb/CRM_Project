from django.contrib import admin

from .models import Product, OrganizationProduct

my_models = [Product, OrganizationProduct]
admin.site.register(my_models)
