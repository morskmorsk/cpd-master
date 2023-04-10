from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Manufacturer, Brand, DeviceModel
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


# create views for Brand model
# class Brand(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)


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


# class DeviceModel(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model_series = models.CharField(max_length=50, default="N/A")
#     name = models.CharField(max_length=50)

# create views for DeviceModel model


# class DeviceModelListView(ListView):
#     model = DeviceModel
#     template_name = 'store/devicemodel/devicemodel_list.html'

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.order_by('brand__manufacturer__name', 'brand__name', 'name')


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