from django import forms
from .models import Customer, WorkOrder
from django.core.exceptions import ValidationError
import phonenumbers
from phonenumber_field.formfields import PhoneNumberField


from phonenumbers import PhoneNumber


class SearchCustomerForm(forms.Form):
    phone = PhoneNumberField(required=True, label='Phone Number')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone.country_code is None:
            phone.country_code = PhoneNumber().region_code
        if phone.national_number is None:
            raise forms.ValidationError(
                'Please enter a valid phone number without the country code.'
                )
        return phone.national_number


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
