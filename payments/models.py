# payments/models.py
from django.db import models
from users.models import User
from jobs.models import JobPost

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('ESEWA', 'eSewa'),
        ('KHALTI', 'Khalti'),
        ('BANK', 'Bank Transfer'),
    )
    
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_made')
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_received')
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Escrow(models.Model):
    job = models.OneToOneField(JobPost, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    released = models.BooleanField(default=False)
    release_date = models.DateTimeField(null=True, blank=True)