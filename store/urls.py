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

app_name = 'store'

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework_home')),
    # manufacturer urls:
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturer/<int:pk>/', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturer/new/', views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturer/<int:pk>/edit/', views.ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturer/<int:pk>/delete/', views.ManufacturerDeleteView.as_view(), name='manufacturer_delete'),
    # brand urls:
    path('brands/', views.BrandListView.as_view(), name='brand_list'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('brand/new/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/edit/', views.BrandUpdateView.as_view(), name='brand_update'), 
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),
    # DeviceModel URLs
    path('devicemodels/', views.DeviceModelListView.as_view(), name='devicemodel_list'),
    path('devicemodel/<int:pk>/', views.DeviceModelDetailView.as_view(), name='devicemodel_detail'),
    path('devicemodel/new/', views.DeviceModelCreateView.as_view(), name='devicemodel_create'),
    path('devicemodel/<int:pk>/edit/', views.DeviceModelUpdateView.as_view(), name='devicemodel_update'),
    path('devicemodel/<int:pk>/delete/', views.DeviceModelDeleteView.as_view(), name='devicemodel_delete'),
    # DeviceColor URLs
    path('devicecolors/', views.DeviceColorListView.as_view(), name='devicecolor_list'),
    path('devicecolor/<int:pk>/', views.DeviceColorDetailView.as_view(), name='devicecolor_detail'),
    path('devicecolor/new/', views.DeviceColorCreateView.as_view(), name='devicecolor_create'),
    path('devicecolor/<int:pk>/edit/', views.DeviceColorUpdateView.as_view(), name='devicecolor_update'),
    path('devicecolor/<int:pk>/delete/', views.DeviceColorDeleteView.as_view(), name='devicecolor_delete'),
    # Vendor URLs
    path('vendors/', views.VendorListView.as_view(), name='vendor_list'),
    path('vendor/<int:pk>/', views.VendorDetailView.as_view(), name='vendor_detail'),
    path('vendor/new/', views.VendorCreateView.as_view(), name='vendor_create'),
    path('vendor/<int:pk>/edit/', views.VendorUpdateView.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete/', views.VendorDeleteView.as_view(), name='vendor_delete'),
    # DeviceDefect URLs
    path('devicedefects/', views.DeviceDefectListView.as_view(), name='devicedefect_list'),
    path('devicedefect/<int:pk>/', views.DeviceDefectDetailView.as_view(), name='devicedefect_detail'),
    path('devicedefect/new/', views.DeviceDefectCreateView.as_view(), name='devicedefect_create'),
    path('devicedefect/<int:pk>/edit/', views.DeviceDefectUpdateView.as_view(), name='devicedefect_update'),
    path('devicedefect/<int:pk>/delete/', views.DeviceDefectDeleteView.as_view(), name='devicedefect_delete'),
    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('department/new/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('department/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('location/new/', views.LocationCreateView.as_view(), name='location_create'),
    path('location/<int:pk>/edit/', views.LocationUpdateView.as_view(), name='location_update'),
    path('location/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),
    # Device URLs
    path('devices/', views.DeviceListView.as_view(), name='device_list'),
    path('device/<int:pk>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/new/', views.DeviceCreateView.as_view(), name='device_create'),
    path('device/<int:pk>/edit/', views.DeviceUpdateView.as_view(), name='device_update'),
    path('device/<int:pk>/delete/', views.DeviceDeleteView.as_view(), name='device_delete'),
    # WorkOrder URLs
    path('workorders/', views.WorkOrderListView.as_view(), name='workorder_list'),
    path('workorder/<int:pk>/', views.WorkOrderDetailView.as_view(), name='workorder_detail'),
    path('workorder/new/', views.WorkOrderCreateView.as_view(), name='workorder_create'),
    path('workorder/<int:pk>/edit/', views.WorkOrderUpdateView.as_view(), name='workorder_update'),
    path('workorder/<int:pk>/delete/', views.WorkOrderDeleteView.as_view(), name='workorder_delete'),
    # WorkOrderItem URLs
    # Labor URLs
    path('labors/', views.LaborListView.as_view(), name='labor_list'),
    path('labor/<int:pk>/', views.LaborDetailView.as_view(), name='labor_detail'),
    path('labor/new/', views.LaborCreateView.as_view(), name='labor_create'),
    path('labor/<int:pk>/edit/', views.LaborUpdateView.as_view(), name='labor_update'),
    path('labor/<int:pk>/delete/', views.LaborDeleteView.as_view(), name='labor_delete'),
    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # Subcategory URLs
    path('subcategories/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/<int:pk>/', views.SubcategoryDetailView.as_view(), name='subcategory_detail'),
    path('subcategory/new/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
    # Tag URLs
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag/new/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    # Product URLs
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # ShoppingCart URLs
    path('shoppingcarts/', views.ShoppingCartListView.as_view(), name='shoppingcart_list'),
    path('shoppingcart/<int:pk>/', views.ShoppingCartDetailView.as_view(), name='shoppingcart_detail'),
    path('shoppingcart/new/', views.ShoppingCartCreateView.as_view(), name='shoppingcart_create'),
    path('shoppingcart/<int:pk>/edit/', views.ShoppingCartUpdateView.as_view(), name='shoppingcart_update'),
    path('shoppingcart/<int:pk>/delete/', views.ShoppingCartDeleteView.as_view(), name='shoppingcart_delete'),
    # CartItem URLs
    path('cartitems/', views.CartItemListView.as_view(), name='cartitem_list'),
    path('cartitem/<int:pk>/', views.CartItemDetailView.as_view(), name='cartitem_detail'),
    path('cartitem/new/', views.CartItemCreateView.as_view(), name='cartitem_create'),
    path('cartitem/<int:pk>/edit/', views.CartItemUpdateView.as_view(), name='cartitem_update'),
    path('cartitem/<int:pk>/delete/', views.CartItemDeleteView.as_view(), name='cartitem_delete'),
]
