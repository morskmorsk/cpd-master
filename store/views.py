from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,\
    DeleteView
from .models import Manufacturer, Brand, DeviceModel,\
    DeviceColor, Vendor, DeviceDefect, Department,\
    Location, Device, WorkOrder, Labor, Category, Subcategory,\
    Tag, Product, ShoppingCart, CartItem
from django.db.models import Prefetch

# create views for Manufacturer model


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'store/manufacturer/manufacturer_list.html'


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'store/manufacturer/manufacturer_detail.html'


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = ['name']
    template_name = 'store/manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('store:manufacturer_list')


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = ['name']
    template_name = 'store/manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('store:manufacturer_list')


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'store/manufacturer/manufacturer_confirm_delete.html'
    success_url = reverse_lazy('store:manufacturer_list')


class BrandListView(ListView):
    model = Brand
    template_name = 'store/brand/brand_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('manufacturer__name', 'name')


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'store/brand/brand_detail.html'


class BrandCreateView(CreateView):
    model = Brand
    fields = ['manufacturer', 'name']
    template_name = 'store/brand/brand_form.html'
    success_url = reverse_lazy('store:brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['manufacturer', 'name']
    template_name = 'store/brand/brand_form.html'
    success_url = reverse_lazy('store:brand_list')


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'store/brand/brand_confirm_delete.html'
    success_url = reverse_lazy('store:brand_list')


class DeviceModelListView(ListView):
    model = DeviceModel
    template_name = 'store/devicemodel/devicemodel_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('brand__manufacturer__name', 'brand__name', 'name')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grouped_devicemodels'] =\
            Manufacturer.objects.all().prefetch_related(
            Prefetch('brand_set__devicemodel_set',
                     queryset=self.get_queryset()))
        return context


class DeviceModelDetailView(DetailView):
    model = DeviceModel
    template_name = 'store/devicemodel/devicemodel_detail.html'


class DeviceModelCreateView(CreateView):
    model = DeviceModel
    fields = ['brand', 'model_series', 'name']
    template_name = 'store/devicemodel/devicemodel_form.html'
    success_url = reverse_lazy('store:devicemodel_list')


class DeviceModelUpdateView(UpdateView):
    model = DeviceModel
    fields = ['brand', 'model_series', 'name']
    template_name = 'store/devicemodel/devicemodel_form.html'
    success_url = reverse_lazy('store:devicemodel_list')


class DeviceModelDeleteView(DeleteView):
    model = DeviceModel
    template_name = 'store/devicemodel/devicemodel_confirm_delete.html'
    success_url = reverse_lazy('store:devicemodel_list')


class DeviceColorListView(ListView):
    model = DeviceColor
    template_name = 'store/devicecolor/devicecolor_list.html'


class DeviceColorDetailView(DetailView):
    model = DeviceColor
    template_name = 'store/devicecolor/devicecolor_detail.html'


class DeviceColorCreateView(CreateView):
    model = DeviceColor
    fields = ['name']
    template_name = 'store/devicecolor/devicecolor_form.html'
    success_url = reverse_lazy('store:devicecolor_list')


class DeviceColorUpdateView(UpdateView):
    model = DeviceColor
    fields = ['name']
    template_name = 'store/devicecolor/devicecolor_form.html'
    success_url = reverse_lazy('store:devicecolor_list')


class DeviceColorDeleteView(DeleteView):
    model = DeviceColor
    template_name = 'store/devicecolor/devicecolor_confirm_delete.html'
    success_url = reverse_lazy('store:devicecolor_list')


class VendorListView(ListView):
    model = Vendor
    template_name = 'store/vendor/vendor_list.html'


class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'store/vendor/vendor_detail.html'


class VendorCreateView(CreateView):
    model = Vendor
    fields = ['name', 'contact_name', 'phone', 'email', 'address']
    template_name = 'store/vendor/vendor_form.html'
    success_url = reverse_lazy('store:vendor_list')


class VendorUpdateView(UpdateView):
    model = Vendor
    fields = ['name', 'contact_name', 'phone', 'email', 'address']
    template_name = 'store/vendor/vendor_form.html'
    success_url = reverse_lazy('store:vendor_list')


class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'store/vendor/vendor_confirm_delete.html'
    success_url = reverse_lazy('store:vendor_list')


class DeviceDefectListView(ListView):
    model = DeviceDefect
    template_name = 'store/devicedefect/devicedefect_list.html'


class DeviceDefectDetailView(DetailView):
    model = DeviceDefect
    template_name = 'store/devicedefect/devicedefect_detail.html'


class DeviceDefectCreateView(CreateView):
    model = DeviceDefect
    fields = ['defect_name', 'defect_description', 'defect_solution']
    template_name = 'store/devicedefect/devicedefect_form.html'
    success_url = reverse_lazy('store:devicedefect_list')


class DeviceDefectUpdateView(UpdateView):
    model = DeviceDefect
    fields = ['defect_name', 'defect_description', 'defect_solution']
    template_name = 'store/devicedefect/devicedefect_form.html'
    success_url = reverse_lazy('store:devicedefect_list')


class DeviceDefectDeleteView(DeleteView):
    model = DeviceDefect
    template_name = 'store/devicedefect/devicedefect_confirm_delete.html'
    success_url = reverse_lazy('store:devicedefect_list')


class DepartmentListView(ListView):
    model = Department
    template_name = 'store/department/department_list.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'store/department/department_detail.html'


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name', 'taxable']
    template_name = 'store/department/department_form.html'
    success_url = reverse_lazy('store:department_list')


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['name', 'taxable']
    template_name = 'store/department/department_form.html'
    success_url = reverse_lazy('store:department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'store/department/department_confirm_delete.html'
    success_url = reverse_lazy('store:department_list')


class LocationListView(ListView):
    model = Location
    template_name = 'store/location/location_list.html'


class LocationDetailView(DetailView):
    model = Location
    template_name = 'store/location/location_detail.html'


class LocationCreateView(CreateView):
    model = Location
    fields = ['name', 'address']
    template_name = 'store/location/location_form.html'
    success_url = reverse_lazy('store:location_list')


class LocationUpdateView(UpdateView):
    model = Location
    fields = ['name', 'address']
    template_name = 'store/location/location_form.html'
    success_url = reverse_lazy('store:location_list')


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'store/location/location_confirm_delete.html'
    success_url = reverse_lazy('store:location_list')


class DeviceListView(ListView):
    model = Device
    template_name = 'store/device/device_list.html'


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'store/device/device_detail.html'


class DeviceCreateView(CreateView):
    model = Device
    fields = ['owner', 'department', 'location', 'device_model',
              'color', 'carrier', 'imei', 'serial_number', 'vendor',
              'seller', 'compatibility', 'cost', 'value', 'price',
              'purchase_date', 'info', 'notes', 'report', 'device_defects',
              'photo', 'status', 'grade']
    template_name = 'store/device/device_form.html'
    success_url = reverse_lazy('store:device_list')


class DeviceUpdateView(UpdateView):
    model = Device
    fields = ['owner', 'department', 'location', 'device_model',
              'color', 'carrier', 'imei', 'serial_number', 'vendor',
              'seller', 'compatibility', 'cost', 'value', 'price',
              'purchase_date', 'info', 'notes', 'report', 'device_defects',
              'photo', 'status', 'grade']
    template_name = 'store/device/device_form.html'
    success_url = reverse_lazy('store:device_list')


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'store/device/device_confirm_delete.html'
    success_url = reverse_lazy('store:device_list')


class WorkOrderListView(ListView):
    model = WorkOrder
    template_name = 'store/workorder/workorder_list.html'


class WorkOrderDetailView(DetailView):
    model = WorkOrder
    template_name = 'store/workorder/workorder_detail.html'


class WorkOrderCreateView(CreateView):
    model = WorkOrder
    fields = ['customer', 'employee', 'device', 'work_order_status', 'price',
              'discount', 'notes']
    template_name = 'store/workorder/workorder_form.html'
    success_url = reverse_lazy('store:workorder_list')


class WorkOrderUpdateView(UpdateView):
    model = WorkOrder
    fields = ['workorder_device', 'workorder_vendor', 'workorder_department',
              'workorder_location', 'workorder_date', 'workorder_notes']
    template_name = 'store/workorder/workorder_form.html'
    success_url = reverse_lazy('store:workorder_list')


class WorkOrderDeleteView(DeleteView):
    model = WorkOrder
    template_name = 'store/workorder/workorder_confirm_delete.html'
    success_url = reverse_lazy('store:workorder_list')


class LaborListView(ListView):
    model = Labor
    template_name = 'store/labor/labor_list.html'


class LaborDetailView(DetailView):
    model = Labor
    template_name = 'store/labor/labor_detail.html'


class LaborCreateView(CreateView):
    model = Labor
    fields = ['labor_vendor', 'labor_department',
              'labor_location', 'labor_date', 'labor_notes']
    template_name = 'store/labor/labor_form.html'
    success_url = reverse_lazy('store:labor_list')


class LaborUpdateView(UpdateView):
    model = Labor
    fields = ['labor_vendor', 'labor_department',
              'labor_location', 'labor_date', 'labor_notes']
    template_name = 'store/labor/labor_form.html'
    success_url = reverse_lazy('store:labor_list')


class LaborDeleteView(DeleteView):
    model = Labor
    template_name = 'store/labor/labor_confirm_delete.html'
    success_url = reverse_lazy('store:labor_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'store/category/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category/category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'taxable']
    template_name = 'store/category/category_form.html'
    success_url = reverse_lazy('store:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'taxable']
    template_name = 'store/category/category_form.html'
    success_url = reverse_lazy('store:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'store/category/category_confirm_delete.html'
    success_url = reverse_lazy('store:category_list')


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'store/subcategory/subcategory_list.html'


class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'store/subcategory/subcategory_detail.html'


class SubcategoryCreateView(CreateView):
    model = Subcategory
    fields = ['name', 'category']
    template_name = 'store/subcategory/subcategory_form.html'
    success_url = reverse_lazy('store:subcategory_list')


class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    fields = ['name', 'category', 'taxable']
    template_name = 'store/subcategory/subcategory_form.html'
    success_url = reverse_lazy('store:subcategory_list')


class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'store/subcategory/subcategory_confirm_delete.html'
    success_url = reverse_lazy('store:subcategory_list')


class TagListView(ListView):
    model = Tag
    template_name = 'store/tag/tag_list.html'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'store/tag/tag_detail.html'


class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'store/tag/tag_form.html'
    success_url = reverse_lazy('store:tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'store/tag/tag_form.html'
    success_url = reverse_lazy('store:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'store/tag/tag_confirm_delete.html'
    success_url = reverse_lazy('store:tag_list')


class ProductListView(ListView):
    model = Product
    template_name = 'store/product/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'sku', 'category',
              'subcategory', 'tags', 'price', 'taxable', 'inventory', 'image']
    template_name = 'store/product/product_form.html'
    success_url = reverse_lazy('store:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'sku', 'category',
              'subcategory', 'tags', 'price', 'taxable', 'inventory', 'image']
    template_name = 'store/product/product_form.html'
    success_url = reverse_lazy('store:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product/product_confirm_delete.html'
    success_url = reverse_lazy('store:product_list')


class ShoppingCartListView(ListView):
    model = ShoppingCart
    template_name = 'store/shoppingcart/shoppingcart_list.html'


class ShoppingCartDetailView(DetailView):
    model = ShoppingCart
    template_name = 'store/shoppingcart/shoppingcart_detail.html'


class ShoppingCartCreateView(CreateView):
    model = ShoppingCart
    fields = ['user', 'product', 'quantity']
    template_name = 'store/shoppingcart/shoppingcart_form.html'
    success_url = reverse_lazy('store:shoppingcart_list')


class ShoppingCartUpdateView(UpdateView):
    model = ShoppingCart
    fields = ['user', 'product', 'quantity']
    template_name = 'store/shoppingcart/shoppingcart_form.html'
    success_url = reverse_lazy('store:shoppingcart_list')


class ShoppingCartDeleteView(DeleteView):
    model = ShoppingCart
    template_name = 'store/shoppingcart/shoppingcart_confirm_delete.html'
    success_url = reverse_lazy('store:shoppingcart_list')


class CartItemListView(ListView):
    model = CartItem
    template_name = 'store/cartitem/cartitem_list.html'


class CartItemDetailView(DetailView):
    model = CartItem
    template_name = 'store/cartitem/cartitem_detail.html'


class CartItemCreateView(CreateView):
    model = CartItem
    fields = ['cart', 'product', 'quantity']
    template_name = 'store/cartitem/cartitem_form.html'
    success_url = reverse_lazy('store:cartitem_list')


class CartItemUpdateView(UpdateView):
    model = CartItem
    fields = ['cart', 'product', 'quantity']
    template_name = 'store/cartitem/cartitem_form.html'
    success_url = reverse_lazy('store:cartitem_list')


class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'store/cartitem/cartitem_confirm_delete.html'
    success_url = reverse_lazy('store:cartitem_list')
