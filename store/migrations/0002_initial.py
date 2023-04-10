# Generated by Django 4.1.5 on 2023-04-10 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_order_Customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_order_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='order_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_order_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='order_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_order_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='cashier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_cashier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shopping_cart_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shopping_cart_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='department', to='store.department'),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='location', to='store.location'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='store.manufacturer'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='product_updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='store.tag'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='store.vendor'),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
        ),
        migrations.AddField(
            model_name='device',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.devicecolor'),
        ),
        migrations.AddField(
            model_name='device',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_department', to='store.department'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='device_defects',
            field=models.ManyToManyField(default=None, help_text='Select all that apply', related_name='device_defects', to='store.devicedefect'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.devicemodel'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.location'),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_vendor', to='store.vendor'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='shopping_cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='store.shoppingcart'),
        ),
        migrations.AddField(
            model_name='brand',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.manufacturer'),
        ),
    ]