from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from Operation.models import *

# Create your models here.

class OfferStatus(models.Model):
    name = models.CharField(max_length=50, default='')
    namear = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Statuses"

class OfferSale(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT)
    status = models.ForeignKey(OfferStatus, on_delete=models.PROTECT)
    offerdate = models.DateField(blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class Sales(models.Model):
    offer = models.ForeignKey(OfferSale, on_delete=models.PROTECT)
    subscriber = models.ForeignKey(User, on_delete=models.PROTECT)
    salesdate = models.DateField(blank=True)
    finalprice = models.DecimalField(max_digits=10, decimal_places=1)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Sales"