from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)


class AnimalClass(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(verbose_name='name arabic', max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', verbose_name='description arabic', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"


class Animals(models.Model):
    animalclass = models.ForeignKey(AnimalClass, on_delete=models.PROTECT,verbose_name='class animal', null=False)
    name = models.CharField(max_length=50)
    namear = models.CharField(verbose_name='name arabic', max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='',verbose_name='description arabic', blank=True)

    family = models.ManyToManyField('Family', through='AnimalFamily')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Animals"


class Family(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(verbose_name='description arabic',max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', verbose_name='description arabic', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Families"


class AnimalFamily(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.PROTECT)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.animals.name + ' ' + self.family.name


class AnimalFamily_Inline(admin.TabularInline):
    model = AnimalFamily
    extra = 1


class Animal(models.Model):
    animalclass = models.ForeignKey(AnimalClass, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50)
    namear = models.CharField(verbose_name='name arabic',max_length=50)
    birthdate = models.DateField(default=datetime.now, blank=True)
    isactive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.PROTECT,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Animal"

    # def save(self, *args, **kwargs):
    #     user = User.objects.filter(username=get_current_authenticated_user())
    #
    #     self.user = user[0]
    #     super(Animal, self).save(*args, **kwargs)

