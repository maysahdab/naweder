from django.db import models
from Animal.models import *
from django.contrib.auth.models import User
# Create your models here.

# from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

def animal_images_upload_path(instance, file_name):
    return f"animal-picture/{file_name}"


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
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def limitanimal():

    user = User.objects.filter(username=get_current_authenticated_user())
    try:
        if (user[0].is_superuser):
            return {}
        else:
            return {'user': user[0]}
    except:
        return {'user': user[0]}

    # return {}
class Operation(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, null=False,limit_choices_to = limitanimal)

    operationdate = models.DateField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.animal.name
    def save(self, *args, **kwargs):
        user = User.objects.filter(username=get_current_authenticated_user())

        self.user = user[0]
        super(Operation, self).save(*args, **kwargs)

class Certificate(models.Model):
    type = models.ForeignKey(CertificateType, on_delete=models.PROTECT, null=False)
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    number = models.PositiveIntegerField()
    certificatedate = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type.name

class Certificateinline(admin.TabularInline):
    fields = ( 'type', 'operation', 'number', 'certificatedate',)
    model = Certificate
    extra = 1

class Pictures(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    image = models.ImageField(upload_to=animal_images_upload_path)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Pictures"

class Picturesinline(admin.TabularInline):
    fields = ( 'operation', 'image', )
    model = Pictures
    extra = 1

class Vaccines(models.Model):
    type = models.ForeignKey(VaccineType, on_delete=models.PROTECT, null=False)
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    number = models.PositiveIntegerField()
    vaccinedate = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name_plural = "Vaccines"

class Vaccinesinline(admin.TabularInline):
    fields = ( 'type', 'operation', 'number', 'vaccinedate',)
    model = Vaccines
    extra = 1

class ReviewOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reviews Operations"