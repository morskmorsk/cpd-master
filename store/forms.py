from django import forms
from .models import Customer, WorkOrder
from django.core.exceptions import ValidationError
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


class SearchCustomerForm(forms.Form):
    phone = forms.CharField(max_length=20, label='Phone Number')

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        default_region = 'US'  # set a default region here
        try:
            parsed_number = phonenumbers.parse(phone_number, default_region)
        except NumberParseException:
            raise forms.ValidationError('Please enter a valid phone number.')

        if not phonenumbers.is_valid_number(parsed_number):
            raise forms.ValidationError('Please enter a valid phone number.')

        return phonenumbers.format_number(parsed_number,
                                          phonenumbers.PhoneNumberFormat.E164)


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone', 'address', 'city', 'state',
                  'zipcode', 'service_provider']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        try:
            parsed_phone = phonenumbers.parse(phone, 'US')
            # Assuming the phone numbers are from the United States
        except phonenumbers.NumberParseException:
            raise ValidationError('Invalid phone number format.')

        if not phonenumbers.is_valid_number(parsed_phone):
            raise ValidationError('Invalid phone number.')

        return phonenumbers.format_number(
            parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)


class AddWorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['price', 'notes']
