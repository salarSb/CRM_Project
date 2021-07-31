from django.contrib import admin

from sale.models import Quote, QuoteItem


class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 0


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_on')
    list_filter = ('owner',)
    inlines = (QuoteItemInline,)
