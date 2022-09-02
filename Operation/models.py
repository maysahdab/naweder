from django.db import models
from Animal.models import *
from django.contrib.auth.models import User
# Create your models here.
from currencyapp.models import Currency
# from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)


def animal_images_upload_path(instance, file_name):
    return f"animal-picture/{file_name}"


Rate_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class CertificateType(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VaccineType(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(verbose_name='Name Arabic',max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(verbose_name='Description Arabic',max_length=250, default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def limitanimal():

    user = User.objects.filter(username=get_current_authenticated_user())
    try:
        if (user[0].is_superuser):
            return {'isactive':True}
        else:
            return {'user': user[0],'isactive':True}
    except:
        return {'user': user[0],'isactive':True}

    # return {}

class Operation(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, null=False,) # limit_choices_to = limitanimal
    operationdate = models.DateField(verbose_name='Operation Date', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    type = (('Auction', 'Auction'),('Sale', 'Sale'))

    operationtype = models.CharField(max_length=10, choices=type, default='Auction')

    def __str__(self):
        return self.animal.name
    #
    # def save(self, *args, **kwargs):
    #     user = User.objects.filter(username=get_current_authenticated_user())
    #
    #     self.user = user[0]
    #     super(Operation, self).save(*args, **kwargs)


class Certificate(models.Model):
    type = models.ForeignKey(CertificateType, on_delete=models.PROTECT, null=False)
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    number = models.PositiveIntegerField()
    certificatedate = models.DateField(verbose_name='Certificate Date',null=True, blank=True)
    image = models.ImageField(verbose_name='Certificate Image',null=True, blank=True,default='gallery.jpg')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type.name


class Certificateinline(admin.TabularInline):
    fields = ('type', 'operation', 'number', 'certificatedate','image')
    model = Certificate
    extra = 1


class Pictures(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    image = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Pictures"


class RefundRequestOperation(models.Model):
    refunddate = models.DateField(verbose_name='Refund Date',)
    operation = models.ForeignKey(Operation,verbose_name='Operation Refund', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class RefundOperation(models.Model):
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='',verbose_name='description arabic', blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    refund = models.ForeignKey(RefundRequestOperation, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Picturesinline(admin.TabularInline):
    fields = ( 'operation', 'image', )
    model = Pictures
    extra = 1


class Vaccines(models.Model):
    type = models.ForeignKey(VaccineType, on_delete=models.PROTECT, null=False)
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    number = models.PositiveIntegerField()
    vaccinedate = models.DateField(verbose_name='Vaccine Date',null=True, blank=True)
    image = models.ImageField(verbose_name='Vaccine Image',null=True, blank=True,default='gallery.jpg')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name_plural = "Vaccines"


class Vaccinesinline(admin.TabularInline):
    fields = ( 'type', 'operation', 'number', 'vaccinedate','image')
    model = Vaccines
    extra = 1


class ReviewOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rate = models.PositiveIntegerField(choices=Rate_CHOICES, default=1)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(verbose_name='Description Arabic',max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.operation.id)

    class Meta:
        verbose_name_plural = "Reviews Operations"

