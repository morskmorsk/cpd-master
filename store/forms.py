from django import forms
from .models import Customer
from django.core.exceptions import ValidationError
import phonenumbers

class SearchCustomerForm(forms.Form):
    phone = forms.CharField(max_length=20, required=True, label='Phone Number')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'service_provider']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        try:
            parsed_phone = phonenumbers.parse(phone, 'US')  # Assuming the phone numbers are from the United States
        except phonenumbers.NumberParseException:
            raise ValidationError('Invalid phone number format.')

        if not phonenumbers.is_valid_number(parsed_phone):
            raise ValidationError('Invalid phone number.')

        return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
