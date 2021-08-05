from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import F, FloatField, Max, ExpressionWrapper

from sale import enums


class Quote(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'quote #{self.pk} submitted by {self.owner.get_full_name()}'

    def get_total_price(self):
        price = self.quoteitem_set.all().annotate(price=F('product__price') * F('qty')).aggregate(Max('price'))[
            'price__max']
        total_price = self.quoteitem_set.all().annotate(total_price=ExpressionWrapper(
            price + ((F('tax') / Decimal('100.0')) * price) - (
                    (F('discount') / Decimal('100.0')) * price), output_field=FloatField()), )
        return total_price.aggregate(Max('total_price'))['total_price__max']


class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    tax = models.PositiveIntegerField(default=9)
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    @property
    def price(self):
        return self.product.price * self.qty

    def get_costumer_name(self):
        return self.organization.owner_of_organization


class EmailHistory(models.Model):
    receiver = models.ForeignKey('organizations.Organization', on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=enums.EmailStatuses.choices)
    send_date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.receiver.owner_of_organization

    class Meta:
        verbose_name = 'Email History'
        verbose_name_plural = 'Email Histories'


class FollowUp(models.Model):
    registrar_user = models.ForeignKey(User, on_delete=models.PROTECT)
    submit_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
