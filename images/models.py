from django.db import models
from web3auth.models import Web3UserMixin
from web3 import Web3

class Image(models.Model):
    title = models.CharField(max_length=128)
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CustomUser(Web3UserMixin, models.Model):
    # Add any additional fields or methods here
    pass
    
    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title}"
