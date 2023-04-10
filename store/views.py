# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse_lazy
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, FormView, UpdateView
# from django.views.generic.list import ListView

# from users.models import CustomUser

# from .forms import AddCustomerForm, AddWorkOrderForm, SearchCustomerForm
# from .models import WorkOrder


# class SearchCustomerView(FormView):
#     template_name = 'store/customers/search_customer.html'
#     form_class = SearchCustomerForm

#     def form_valid(self, form):
#         phone = form.cleaned_data['phone']
#         customer = CustomUser.objects.filter(phone=phone).first()

#         if customer:
#             return redirect('customer_detail', customer_id=customer.id)
#         else:
#             customer_form = AddCustomerForm(initial={'phone': phone})
#             return render(self.request, 'store/customers/add_customer.html',
#                           {'customer_form': customer_form})


# class CustomerDetailView(DetailView):
#     model = CustomUser
#     template_name = 'store/customers/customer_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['customer'] = self.object
#         context['pk'] = self.object.pk  # Pass the pk value to the template
#         return context


# class AddCustomerView(CreateView):
#     model = CustomUser
#     form_class = AddCustomerForm
#     template_name = 'store/customers/add_customer.html'

#     def get_success_url(self):
#         return reverse_lazy('customer_detail', kwargs={'pk': self.object.pk})


# class EditCustomerView(UpdateView):
#     model = CustomUser
#     form_class = AddCustomerForm
#     template_name = 'store/customers/edit_customer.html'
#     context_object_name = 'customer'

#     def get_success_url(self):
#         return reverse_lazy('customer_detail',
#                             kwargs={'customer_id': self.object.id})


# class AddWorkOrderView(UserPassesTestMixin, CreateView):
#     model = WorkOrder
#     form_class = AddWorkOrderForm
#     template_name = 'store/work_orders/add_workorder.html'
#     # You should provide the correct template name here

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         # Redirect the user to the login page if they are not authenticated
#         return redirect('login')  # Use the correct name for your login view

#     def form_valid(self, form):
#         work_order = form.save(commit=False)
#         work_order.customer = get_object_or_404(
#             Customer, pk=self.kwargs['customer_id']
#             )
#         work_order.employee = self.request.user
#         work_order.save()
#         return redirect('customer_work_orders',
#         pk=self.kwargs['customer_id'])
#         # return redirect('store/work_orders/customer_work_orders.html',
#         #                 customer_id=self.kwargs['customer_id'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['customer'] = get_object_or_404(
#             Customer, pk=self.kwargs['customer_id']
#             )
#         return context


# class CustomerWorkOrdersView(ListView):
#     model = WorkOrder
#     template_name = 'store/customers/customer_work_orders.html'
#     context_object_name = 'work_orders'

#     def get_queryset(self):
#         customer = get_object_or_404(Customer, pk=self.kwargs['customer_id'])
#         return WorkOrder.objects.filter(customer=customer)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['customer'] = get_object_or_404(
#             Customer, pk=self.kwargs['customer_id']
#             )
#         return context
