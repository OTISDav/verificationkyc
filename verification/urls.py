from django.urls import path
from .views import KYCVerificationView

urlpatterns = [
    path('verify/', KYCVerificationView.as_view(), name='kyc_verify'),
]
