from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Manufacturer, Brand, DeviceModel, DeviceColor, Vendor
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
        context['grouped_devicemodels'] = Manufacturer.objects.all().prefetch_related(Prefetch('brand_set__devicemodel_set', queryset=self.get_queryset()))
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
