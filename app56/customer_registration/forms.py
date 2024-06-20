from django import forms
from .models import Customer, SavingsAccount, MFAccount, LoanAccount

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'aadhaar', 'pincode']

class SavingsAccountForm(forms.ModelForm):
    class Meta:
        model = SavingsAccount
        fields = ['customer', 'initial_amount']

class MFAccountForm(forms.ModelForm):
    class Meta:
        model = MFAccount
        fields = ['customer', 'mf_scheme', 'investment_amount']

class LoanAccountForm(forms.ModelForm):
    class Meta:
        model = LoanAccount
        fields = ['customer', 'loan_amount', 'loan_type', 'interest_rate', 'duration_months']
