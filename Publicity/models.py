from django.db import models
from django.contrib.auth.models import User
from currencyapp.models import Currency
from django.contrib import admin
from Address.models import Street


class Service(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50, verbose_name='name arabic')
    descriptionar = models.CharField(max_length=25, blank=True, verbose_name='description arabic')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TypePublicity(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50, verbose_name='name arabic')
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True, verbose_name='name arabic')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Type Publicities"


class Publicity(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True, verbose_name='description arabic')
    price = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    phone = models.CharField(max_length=15, blank=True)
    fromdate = models.DateTimeField(auto_now_add=True)
    todate = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    service = models.ManyToManyField(Service, through='PublicityService')
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    type = models.ForeignKey(TypePublicity, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Publicities"

    def __str__(self):
        return self.type.name


class PublicityService(models.Model):
    publicity = models.ForeignKey(Publicity, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class PublicityService_Inline(admin.TabularInline):
    model = PublicityService
    extra = 1


class ImagePublicity(models.Model):
    image = models.ImageField()
    publicity = models.ForeignKey(Publicity, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images Publicities"


class ImagePublicitysinline(admin.TabularInline):
    fields = ('image','publicity',)
    model = ImagePublicity
    extra = 1