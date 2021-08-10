from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import F, FloatField, Max, ExpressionWrapper
from django.utils.translation import ugettext_lazy as _

from sale import enums


class Quote(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name=_('owner'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('created on'))

    def __str__(self):
        return f'{_("quote")} #{self.pk} {_("submitted by")} {self.owner.get_full_name()}'

    def get_total_price(self):
        price = self.quoteitem_set.all().annotate(price=F('product__price') * F('qty')).aggregate(Max('price'))[
            'price__max']
        total_price = self.quoteitem_set.all().annotate(total_price=ExpressionWrapper(
            price + ((F('tax') / Decimal('100.0')) * price) - (
                    (F('discount') / Decimal('100.0')) * price), output_field=FloatField()), )
        return total_price.aggregate(Max('total_price'))['total_price__max']


class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name=_('quote'))
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE,
                                     verbose_name=_('organization'))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name=_('product'))
    qty = models.PositiveIntegerField(default=1, verbose_name=_('quantity'))
    tax = models.PositiveIntegerField(default=9, verbose_name=_('tax'))
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name=_('discount'))

    @property
    def price(self):
        return self.product.price * self.qty

    def get_costumer_name(self):
        return self.organization.owner_of_organization


class EmailHistory(models.Model):
    receiver = models.ForeignKey('organizations.Organization', on_delete=models.PROTECT, verbose_name=_('receiver'))
    status = models.CharField(max_length=1, choices=enums.EmailStatuses.choices, verbose_name=_('status'))
    send_date = models.DateTimeField(auto_now_add=True, verbose_name=_('send date'))
    sender = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('sender'))

    def __str__(self):
        return self.receiver.owner_of_organization

    class Meta:
        verbose_name = _('Email History')
        verbose_name_plural = _('Email Histories')


class FollowUp(models.Model):
    registrar_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('registrar user'))
    organization = models.ForeignKey('organizations.Organization', on_delete=models.PROTECT,
                                     verbose_name=_('organization'))
    submit_date = models.DateTimeField(auto_now_add=True, verbose_name=_('submit date'))
    description = models.TextField(verbose_name=_('description'))
