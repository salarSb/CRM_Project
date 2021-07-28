from django.contrib import admin

from .models import Product, OrganizationProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'taxable']
    list_display_links = ['id', 'name']
    sortable_by = 'price'
    list_filter = ['usable_for_organization_product', 'taxable']
    fieldsets = (
        ('Identification', {
            'fields': ('name', 'price', 'taxable')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('image', 'catalog', 'technical_features', 'usable_for_organization_product',)
        }),
    )
    list_editable = ['taxable']
    actions = ['make_without_tax']

    def make_without_tax(self, request, queryset):
        updated = queryset.update(taxable=False)

    make_without_tax.short_description = 'No Tax'


@admin.register(OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['slug']
    list_display_links = ['id', 'name']
    sortable_by = 'name'
