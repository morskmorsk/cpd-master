from django.urls import path, include
from rest_framework import routers
from . import views
from .api_views import (ManufacturerViewSet, BrandViewSet,
                        DeviceModelViewSet, DeviceColorViewSet,
                        VendorViewSet, DeviceDefectViewSet,
                        DepartmentViewSet, LocationViewSet,
                        DeviceViewSet, WorkOrderViewSet,
                        LaborViewSet, CategoryViewSet,
                        SubcategoryViewSet, TagViewSet,
                        ProductViewSet, ShoppingCartViewSet,
                        CartItemViewSet)

router = routers.DefaultRouter()

router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'devicemodels', DeviceModelViewSet)
router.register(r'devicecolors', DeviceColorViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'devicedefects', DeviceDefectViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'workorders', WorkOrderViewSet)
router.register(r'labor', LaborViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'products', ProductViewSet)
router.register(r'shoppingcarts', ShoppingCartViewSet)
router.register(r'cartitems', CartItemViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework_home')),
    # manufacturer urls:
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturer/<int:pk>/', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturer/new/', views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturer/<int:pk>/edit/', views.ManufacturerUpdateView.as_view(), name='manufacturer_update'),
]
