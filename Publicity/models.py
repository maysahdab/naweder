from django.db import models
from django.contrib.auth.models import User
from currencyapp.models import Currency
from django.contrib import admin
from Address.models import Street


class Service(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    descriptionar = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TypePublicity(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    descriptionar = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Type Publicities"


class Publicity(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    fromdate = models.DateTimeField(auto_now_add=True)
    todate = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False, blank=True)
    service = models.ManyToManyField(Service, through='PublicityService', blank=True)
    street = models.ForeignKey(Street, on_delete=models.PROTECT, blank=True)
    type = models.ForeignKey(TypePublicity, on_delete=models.PROTECT, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Publicities"


class PublicityService(models.Model):
    publicity = models.ForeignKey(Publicity, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class PublicityService_Inline(admin.TabularInline):
    model = PublicityService
    extra = 1


class ImagePublicity(models.Model):
    image = models.ImageField()
    publicity = models.ForeignKey(Publicity, on_delete=models.PROTECT, related_name='image_pub')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images Publicities"
