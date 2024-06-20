from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, SavingsAccountForm, MFAccountForm, LoanAccountForm
from .models import Customer

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('product_selection', customer_id=customer.customer_id)
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer_reg/register.html', {'form': form})

def product_selection(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    return render(request, 'customer_reg/product.html', {'customer': customer})

def open_savings_account(request):
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SavingsAccountForm()
    return render(request, 'customer_reg/savings_account.html', {'form': form})

def open_mf_account(request):
    if request.method == 'POST':
        form = MFAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MFAccountForm()
    return render(request, 'customer_reg/mf_account.html', {'form': form})

def open_loan_account(request):
    if request.method == 'POST':
        form = LoanAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = LoanAccountForm()
    return render(request, 'customer_reg/loan_account.html', {'form': form})

def success(request):
    return render(request, 'customer_reg/success.html')
