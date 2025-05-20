from django.db import models

class KYCRequest(models.Model):
    id_document = models.ImageField(upload_to="kyc_docs/")
    selfie = models.ImageField(upload_to="kyc_selfies/")
    id_number_input = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
