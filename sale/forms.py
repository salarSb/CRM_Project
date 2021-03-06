from django import forms

from organizations.models import Organization
from sale.models import QuoteItem, FollowUp


class QuoteItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(QuoteItemForm, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(submit_user=self.request.user)

    class Meta:
        model = QuoteItem
        fields = ['organization', 'product', 'qty', 'tax', 'discount']


class FollowUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FollowUpForm, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(submit_user=self.request.user)

    class Meta:
        model = FollowUp
        fields = ['organization', 'description']
