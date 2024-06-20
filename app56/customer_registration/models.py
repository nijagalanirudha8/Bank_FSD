from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    aadhaar = models.CharField(max_length=12, unique=True)
    pincode = models.CharField(max_length=6)
    customer_id = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.all().order_by('-id').first()
            if last_customer:
                last_id = int(last_customer.customer_id.split('_')[1])
            else:
                last_id = 5000
            self.customer_id = f'CID_{last_id + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_id

class SavingsAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)

class MFAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mf_scheme = models.CharField(max_length=100)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)

class LoanAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_type = models.CharField(max_length=50)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
