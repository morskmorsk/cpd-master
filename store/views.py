from django.shortcuts import render
from .models import Customer, WorkOrder
from .forms import SearchCustomerForm, AddCustomerForm, AddWorkOrderForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


class SearchCustomerView(FormView):
    template_name = 'store/search_customer.html'
    form_class = SearchCustomerForm

    def form_valid(self, form):
        phone = form.cleaned_data['phone']
        customer = Customer.objects.filter(phone=phone).first()

        if customer:
            return redirect('customer_detail', customer_id=customer.id)
        else:
            customer_form = AddCustomerForm(initial={'phone': phone})
            return render(self.request, 'store/add_customer.html',
                          {'customer_form': customer_form})


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'store/customer_detail.html'
    context_object_name = 'customer'


class AddCustomerView(CreateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'store/add_customer.html'

    def get_success_url(self):
        return reverse_lazy('customer_detail',
                            kwargs={'customer_id': self.object.id})


class EditCustomerView(UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'store/edit_customer.html'
    context_object_name = 'customer'

    def get_success_url(self):
        return reverse_lazy('customer_detail',
                            kwargs={'customer_id': self.object.id})


class AddWorkOrderView(UserPassesTestMixin, CreateView):
    model = WorkOrder
    form_class = AddWorkOrderForm
    template_name = 'store/add_workorder.html'
    # You should provide the correct template name here

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Redirect the user to the login page if they are not authenticated
        return redirect('login')  # Use the correct name for your login view

    def form_valid(self, form):
        work_order = form.save(commit=False)
        work_order.customer = get_object_or_404(
            Customer, pk=self.kwargs['customer_id']
            )
        work_order.employee = self.request.user
        work_order.save()
        return redirect('store/customer_work_orders.html',
                        customer_id=self.kwargs['customer_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = get_object_or_404(
            Customer, pk=self.kwargs['customer_id']
            )
        return context


class CustomerWorkOrdersView(ListView):
    model = WorkOrder
    template_name = 'store/customer_work_orders.html'
    context_object_name = 'work_orders'

    def get_queryset(self):
        customer = get_object_or_404(Customer, pk=self.kwargs['customer_id'])
        return WorkOrder.objects.filter(customer=customer)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = get_object_or_404(
            Customer, pk=self.kwargs['customer_id']
            )
        return context
