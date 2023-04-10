from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets
from .models import Manufacturer
from .serializers import ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


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
    success_url = reverse_lazy('manufacturer_list')


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = ['name']
    template_name = 'store/manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('manufacturer_list')
