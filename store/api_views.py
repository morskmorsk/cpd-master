from .models import (Manufacturer, Brand, DeviceModel, DeviceColor, Vendor,
                     DeviceDefect, Department, Location)
from .models import (Device, WorkOrder, Labor, Category, Subcategory, Tag)
from .models import Product, ShoppingCart, CartItem

from .serializers import (ManufacturerSerializer, BrandSerializer,
                          DeviceModelSerializer, DeviceColorSerializer,
                          VendorSerializer, DeviceDefectSerializer,
                          DepartmentSerializer, LocationSerializer,
                          DeviceSerializer, WorkOrderSerializer,
                          LaborSerializer, CategorySerializer,
                          SubcategorySerializer,
                          TagSerializer, ProductSerializer,
                          ShoppingCartSerializer,
                          CartItemSerializer)
from rest_framework import viewsets


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer
    
    
class DeviceColorViewSet(viewsets.ModelViewSet):
    queryset = DeviceColor.objects.all()
    serializer_class = DeviceColorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class DeviceDefectViewSet(viewsets.ModelViewSet):
    queryset = DeviceDefect.objects.all()
    serializer_class = DeviceDefectSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer


class LaborViewSet(viewsets.ModelViewSet):
    queryset = Labor.objects.all()
    serializer_class = LaborSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
