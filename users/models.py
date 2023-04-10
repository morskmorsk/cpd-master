import phonenumbers
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


STATE_CHOICES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
)

SERVICE_PROVIDER_CHOICES = (
    ('AT&T', 'AT&T'),
    ('T-Mobile', 'T-Mobile'),
    ('Verizon', 'Verizon'),
    ('Metro', 'Metro'),
    ('Cricket', 'Cricket'),
    ('Simple Mobile', 'Simple Mobile'),
    ('H20', 'H20'),
    ('Lyca Mobile', 'Lyca Mobile'),
    ('Ultra Mobile', 'Ultra Mobile'),
    ('Net 10', 'Net 10'),
    ('Straight Talk', 'Straight Talk'),
    ('Tracfone', 'Tracfone'),
    ('Boost Mobile', 'Boost Mobile'),
    ('Virgin Mobile', 'Virgin Mobile'),
    ('Sprint', 'Sprint'),
    ('Other', 'Other'),
    ('Unknown', 'Unknown'),
)


def validate_phone_number(value):
    try:
        if not value.startswith("+"):
            value = "+1" + value  # Add US country code
        print(f"Parsing phone number: {value}")
        parsed_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError('Invalid phone number')
    except phonenumbers.NumberParseException:
        raise ValidationError('Invalid phone number')


class CustomUserManager(BaseUserManager):
    def create_user(self, phoneNumber, password=None, **extra_fields):
        if not phoneNumber:
            raise ValueError('The phoneNumber field must be set')

        # Add the default region code 'US' to the phone number
        parsed_number = phonenumbers.parse(phoneNumber, 'US')
        phoneNumber = phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.E164)

        # Check if the phone number is unique
        if CustomUser.objects.filter(phoneNumber=phoneNumber).exists():
            raise ValueError('The phoneNumber field must be unique')

        user = self.model(phoneNumber=phoneNumber, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # ...

    def create_superuser(self, phoneNumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(phoneNumber, password, **extra_fields)
        return user


class CustomUser(AbstractBaseUser):
    phone_regex = RegexValidator(
        regex=r"^\d{10,15}$",
        message=_("Phone number must be entered in the format:\
                  '9999999999'. Up to 15 digits allowed.")
    )
    phoneNumber = models.CharField(
        validators=[phone_regex, validate_phone_number],
        max_length=15,
        unique=True  # Remove unique=True
    )
    # ...
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    service_provider = models.CharField(
        max_length=50,
        choices=SERVICE_PROVIDER_CHOICES,
        default='Unknown'
    )
    accept_devices_trade_in = models.BooleanField(default=True)
    accept_devices_buy = models.BooleanField(default=True)
    accept_devices_sell = models.BooleanField(default=True)
    accept_device_repair = models.BooleanField(default=True)
    accept_purchase = models.BooleanField(default=True)
    blacklisted = models.BooleanField(default=False)
    blacklisted_reason = models.CharField(
        max_length=100, default="", blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/profile_pics', blank=True, null=True)
    notes = models.TextField(max_length=500, blank=True, default="")
    bio = models.TextField(max_length=500, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.phoneNumber

    def has_perm(self, perm, obj=None):
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        return super().has_module_perms(app_label)
