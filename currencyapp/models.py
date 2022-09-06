import datetime
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    symbol = models.CharField(max_length=4)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "currencies"

