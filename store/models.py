from django.db import models
from accounts.models import Account
from customer.models import Customer
from django.utils.safestring import mark_safe
import datetime


class Store(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='photos/store', default='../static/assets/images/NO-IMAGE.png')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Spent(models.Model):

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now())
    total = models.FloatField(default=0)
    description = models.CharField(max_length=50,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class DaySpent(models.Model):

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now())
    total = models.FloatField(default=0)
    description = models.CharField(max_length=50,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Sale(models.Model):

    CARRIER = (
        ('NA', 'NA'),
        ('Envia', 'Envia'),
        ('InterRapidisimo', 'InterRapidisimo'),
        ('Servientrega', 'Servientrega'),
        ('Domiclio', 'Domicilio')
    )

    STATUS = (
        ('NEW', 'Nuevo'),
        ('CANCELLED', 'Cancelado'),
        ('COMPLETE', 'Completado')
    )
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    sale = models.TextField(blank=True)
    amount = models.IntegerField(default=1)
    collection = models.FloatField(default=0, blank=False)
    cost = models.FloatField(default=0, blank=False)
    date = models.DateField(default=datetime.datetime.now())
    carrier = models.CharField(max_length=50, choices=CARRIER, default='NA')
    guide = models.CharField(max_length=50)
    freight = models.FloatField(default=0, blank=False)
    status = models.CharField(max_length=50, choices=STATUS, default='NEW')
    delivery_status = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.guide
