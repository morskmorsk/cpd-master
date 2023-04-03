from django.db import models
from django.contrib.auth.models import User


SERVICE_PROVIDER_CHOICES = (
    ('N/A', 'n/a'),
    ('At&t', 'at&t'),
    ('T-mobile', 't-mobile'),
    ('Verizon', 'verizon'),
    ('Metro', 'metro'),
    ('Cricket', 'cricket'),
    ('Simple Mobile', 'simple mobile'),
    ('H20', 'h20'),
    ('Lyca Mobile', 'lyca mobile'),
    ('Ultra Mobile', 'ultra mobile'),
    ('Net 10', 'net 10'),
    ('Straight Talk', 'straight talk'),
    ('Tracfone', 'tracfone'),
    ('Boost Mobile', 'boost mobile'),
    ('Virgin Mobile', 'virgin mobile'),
    ('Sprint', 'sprint'),
    ('Unlocked', 'unlocked'),
    ('Other', 'other'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)

STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
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
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)


class Customer(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='Username')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Address')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='City')
    state = models.CharField(max_length=2, blank=True, null=True, choices=STATE_CHOICES, verbose_name='State')
    zipcode = models.CharField(max_length=10, blank=True, null=True, verbose_name='Zip Code')
    service_provider = models.CharField(max_length=50, choices=SERVICE_PROVIDER_CHOICES, default='Unknown', verbose_name='Service Provider')
    accept_devices_trade_in = models.BooleanField(default=True, verbose_name='Accept Trade-ins')
    accept_devices_buy = models.BooleanField(default=True, verbose_name='Buy Devices')
    accept_devices_sell = models.BooleanField(default=True, verbose_name='Sell Devices')
    accept_device_repair = models.BooleanField(default=True, verbose_name='Repair Devices')
    accept_sell = models.BooleanField(default=True, verbose_name='Accept Sales')
    blacklisted = models.BooleanField(default=False, verbose_name='Blacklisted')
    blacklisted_reason = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name='Blacklisted Reason')
    photo = models.ImageField(upload_to='profile_pics', blank=True, null=True, verbose_name='Profile Photo')
    notes = models.TextField(max_length=500, blank=True, null=True, verbose_name='Notes')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='Biography')

    def __str__(self):
        return str(self.user)

    def __repr__(self) -> str:
        return str(self.user)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
