from django.contrib import admin

from sale.models import Quote, QuoteItem, EmailHistory


class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 0


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_on')
    list_filter = ('owner',)
    inlines = (QuoteItemInline,)


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ('receiver', 'status', 'send_date', 'sender')
