from django.db import models
from accounts.models import Account


class Customer(models.Model):

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=50, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
