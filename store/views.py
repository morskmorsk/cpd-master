from django.shortcuts import render
from .models import Customer
from .forms import SearchCustomerForm, CustomerForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def search_customer(request):
    if request.method == 'POST':
        search_form = SearchCustomerForm(request.POST)

        if search_form.is_valid():
            phone = search_form.cleaned_data['phone']
            customer = Customer.objects.filter(phone=phone).first()

            if customer:
                # Redirect to customer detail page or show customer details
                return redirect('customer_detail', customer_id=customer.id)
            else:
                # Render the form to add a new customer
                customer_form = CustomerForm(initial={'phone': phone})
                return render(request, 'store/add_customer.html', {'customer_form': customer_form})

    else:
        search_form = SearchCustomerForm()

    return render(request, 'store/search_customer.html', {'search_form': search_form})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'store/customer_detail.html', {'customer': customer})


def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            # Save the new customer
            new_customer = customer_form.save()

            # Redirect to the customer detail page
            messages.success(request, 'Customer added successfully')
            return redirect('customer_detail', customer_id=new_customer.id)

        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        customer_form = CustomerForm()

    return render(request, 'store/add_customer.html', {'customer_form': customer_form})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully')
            return redirect('customer_detail', customer_id=customer.id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'store/edit_customer.html', {'form': form, 'customer': customer})


def add_work_order(request, customer_id):
    return render(request, 'store/add_workorder.html', {'customer_id': customer_id})


def add_sale(request, customer_id):
    return render(request, 'store/add_sale.html', {'customer_id': customer_id})
