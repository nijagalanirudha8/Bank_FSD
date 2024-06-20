from django.contrib import admin
from .models import Customer, SavingsAccount, MFAccount, LoanAccount

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'aadhaar', 'pincode')
    search_fields = ('customer_id', 'first_name', 'last_name', 'aadhaar')
    list_filter = ('pincode',)

class SavingsAccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'initial_amount')
    search_fields = ('customer__customer_id', 'customer__first_name', 'customer__last_name')
    list_filter = ('initial_amount',)

class MFAccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'mf_scheme', 'investment_amount')
    search_fields = ('customer__customer_id', 'customer__first_name', 'customer__last_name', 'mf_scheme')
    list_filter = ('mf_scheme', 'investment_amount')

class LoanAccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'loan_amount', 'loan_type', 'interest_rate', 'duration_months')
    search_fields = ('customer__customer_id', 'customer__first_name', 'customer__last_name', 'loan_type')
    list_filter = ('loan_type', 'interest_rate', 'duration_months')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(SavingsAccount, SavingsAccountAdmin)
admin.site.register(MFAccount, MFAccountAdmin)
admin.site.register(LoanAccount, LoanAccountAdmin)
