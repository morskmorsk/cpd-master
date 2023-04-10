from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'phoneNumber', 'first_name', 'last_name', 'is_active',
            'is_staff', 'is_superuser', 'email', 'address', 'city', 'state',
            'zipcode', 'service_provider', 'accept_devices_trade_in',
            'accept_devices_buy', 'accept_devices_sell',
            'accept_device_repair', 'accept_purchase', 'blacklisted',
            'blacklisted_reason', 'photo','notes', 'bio', 'created_at',
            'updated_at'
        ]
