from django import forms
from .models import Customer


class SearchCustomerForm(forms.Form):
    phone = forms.CharField(max_length=20, required=True, label='Phone Number')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'service_provider']
