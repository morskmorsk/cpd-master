from django.contrib import admin
from .models import (Manufacturer, Brand, DeviceModel, DeviceColor, Vendor,
                     DeviceDefect, Department, Location)
from .models import (Device, WorkOrder, Labor, Category, Subcategory, Tag)
from .models import Product, ShoppingCart, CartItem

admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(DeviceModel)
admin.site.register(DeviceColor)
admin.site.register(Vendor)
admin.site.register(DeviceDefect)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Device)
admin.site.register(WorkOrder)
admin.site.register(Labor)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
