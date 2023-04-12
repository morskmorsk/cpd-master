from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView,
                                  CreateView)
from .models import CustomUser
from django.urls import reverse_lazy


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'users/customuser_list.html'
    context_object_name = 'customuser_list'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/customuser_detail.html'
    context_object_name = 'customuser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomUserCreateView(LoginRequiredMixin, UserPassesTestMixin,
                           CreateView):
    model = CustomUser
    template_name = 'users/customuser_create.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'address',
        'city',
        'state',
        'zipcode',
        'service_provider',
        'accept_devices_trade_in',
        'accept_devices_buy',
        'accept_devices_sell',
        'accept_device_repair',
        'accept_purchase',
        'blacklisted',
        'blacklisted_reason',
        'photo',
        'notes',
        'bio',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                           UpdateView):
    model = CustomUser
    template_name = 'users/customuser_update.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'address',
        'city',
        'state',
        'zipcode',
        'service_provider',
        'accept_devices_trade_in',
        'accept_devices_buy',
        'accept_devices_sell',
        'accept_device_repair',
        'accept_purchase',
        'blacklisted',
        'blacklisted_reason',
        'photo',
        'notes',
        'bio',
    ]

    success_url = reverse_lazy('users_list')  # Add this line

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class CustomUserDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                           DeleteView):
    model = CustomUser
    template_name = 'users/customuser_delete.html'
    success_url = '/users/'

    def test_func(self):
        return self.request.user.is_superuser
