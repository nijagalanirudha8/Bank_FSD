from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register_customer'),
    path('products/<str:customer_id>/', views.product_selection, name='product_selection'),
    path('savings-account/', views.open_savings_account, name='open_savings_account'),
    path('mf-account/', views.open_mf_account, name='open_mf_account'),
    path('loan-account/', views.open_loan_account, name='open_loan_account'),
    path('success/', views.success, name='success'),
]
