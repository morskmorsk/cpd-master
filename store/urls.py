from django.urls import path
from . import views

urlpatterns = [
    # your other URL patterns
    path('', views.search_customer, name='search_customer'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('add_work_order/<int:customer_id>/', views.add_work_order, name='add_work_order'),
    path('add_sale/<int:customer_id>/', views.add_sale, name='add_sale'),
]
