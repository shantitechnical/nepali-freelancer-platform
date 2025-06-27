# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('FREELANCER', 'Freelancer'),
        ('CLIENT', 'Client'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)
    nepali_language_preference = models.BooleanField(default=False)

class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField('jobs.Skill')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    experience = models.PositiveIntegerField(default=0)  # in years

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    company_website = models.URLField(blank=True)

class KYCDocument(models.Model):
    DOCUMENT_TYPES = (
        ('CITIZENSHIP', 'Citizenship'),
        ('LICENSE', 'License'),
        ('PASSPORT', 'Passport'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    document_front = models.ImageField(upload_to='kyc/')
    document_back = models.ImageField(upload_to='kyc/')
    verified = models.BooleanField(default=False)
    verification_date = models.DateTimeField(null=True, blank=True)