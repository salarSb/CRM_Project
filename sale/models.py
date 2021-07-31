from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Sum


class Quote(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'quote #{self.pk} submitted by {self.owner.get_full_name()}'

    def get_price_without_tax(self):
        return self.quoteitem_set.all().annotate(total_price=F('qty') * F('price')).aggregate((Sum('total_price')))[
            'total_price__sum']

    def get_price_with_tax(self):
        return self.quoteitem_set.all().annotate(total_price=F('qty') * F('price') * (F('tax') / 100)).aggregate(
            (Sum('total_price')))['total_price__sum']


class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    tax = models.PositiveIntegerField(default=9)

    def get_costumer_name(self):
        return self.organization.owner_of_organization
