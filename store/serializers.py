from rest_framework import serializers
from .models import (Manufacturer, Brand, DeviceModel, DeviceColor, Vendor,
                     DeviceDefect, Department, Location)
from .models import (Device, WorkOrder, Labor, Category, Subcategory, Tag)
from .models import Product, ShoppingCart, CartItem


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Brand
        fields = '__all__'


class DeviceModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = DeviceModel
        fields = '__all__'


class DeviceColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceColor
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class DeviceDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceDefect
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'




class DeviceSerializer(serializers.ModelSerializer):
    device_defects = serializers.StringRelatedField(many=True)

    class Meta:
        model = Device
        fields = '__all__'


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class LaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    item_total = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'item_total']


class ShoppingCartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    tax = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
