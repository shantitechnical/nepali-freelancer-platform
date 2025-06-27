# users/urls.py
from django.urls import path
from .views import UserRegistrationView, FreelancerProfileView, ClientProfileView, KYCDocumentView

urlpatterns = [
    path('', UserRegistrationView.as_view(), name='register'),
    path('freelancer/profile/', FreelancerProfileView.as_view(), name='freelancer-profile'),
    path('client/profile/', ClientProfileView.as_view(), name='client-profile'),
    path('kyc/', KYCDocumentView.as_view(), name='kyc'),
]