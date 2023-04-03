# Generated by Django 4.1.5 on 2023-04-03 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2, null=True, verbose_name='State')),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip Code')),
                ('service_provider', models.CharField(choices=[('N/A', 'n/a'), ('At&t', 'at&t'), ('T-mobile', 't-mobile'), ('Verizon', 'verizon'), ('Metro', 'metro'), ('Cricket', 'cricket'), ('Simple Mobile', 'simple mobile'), ('H20', 'h20'), ('Lyca Mobile', 'lyca mobile'), ('Ultra Mobile', 'ultra mobile'), ('Net 10', 'net 10'), ('Straight Talk', 'straight talk'), ('Tracfone', 'tracfone'), ('Boost Mobile', 'boost mobile'), ('Virgin Mobile', 'virgin mobile'), ('Sprint', 'sprint'), ('Unlocked', 'unlocked'), ('Other', 'other'), ('Unknown', 'unknown'), ('آخر', 'آخر')], default='Unknown', max_length=50, verbose_name='Service Provider')),
                ('accept_devices_trade_in', models.BooleanField(default=True, verbose_name='Accept Trade-ins')),
                ('accept_devices_buy', models.BooleanField(default=True, verbose_name='Buy Devices')),
                ('accept_devices_sell', models.BooleanField(default=True, verbose_name='Sell Devices')),
                ('accept_device_repair', models.BooleanField(default=True, verbose_name='Repair Devices')),
                ('accept_sell', models.BooleanField(default=True, verbose_name='Accept Sales')),
                ('blacklisted', models.BooleanField(default=False, verbose_name='Blacklisted')),
                ('blacklisted_reason', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Blacklisted Reason')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Profile Photo')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Biography')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('id',),
            },
        ),
    ]