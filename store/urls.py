from django.urls import path
from .views import SearchCustomerView, CustomerDetailView, AddCustomerView,\
    EditCustomerView, AddWorkOrderView, CustomerWorkOrdersView

urlpatterns = [
    path('', SearchCustomerView.as_view(),
         name='search_customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(),
         name='customer_detail'),
    path('add_customer/', AddCustomerView.as_view(),
         name='add_customer'),
    path('edit_customer/<int:customer_id>/', EditCustomerView.as_view(),
         name='edit_customer'),
    path('add_work_order/<int:customer_id>/', AddWorkOrderView.as_view(),
         name='add_work_order'),
    path('customer/<int:customer_id>/work_orders/',
         CustomerWorkOrdersView.as_view(),
         name='customer_work_orders'),
]
