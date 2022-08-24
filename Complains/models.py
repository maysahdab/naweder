from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Complains(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Complains"

    def __str__(self):
        return self.user.username + ' ' + self.description


class ImageComplains(models.Model):
    image = models.ImageField()
    complains = models.ForeignKey(Complains, on_delete=models.PROTECT, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images Complains"


class ImageComplainsinline(admin.TabularInline):
    fields = ('image', 'complains',)
    model = ImageComplains
    extra = 1


class Response(models.Model):
    description = models.CharField(max_length=250)
    # descriptionar = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    complains = models.ForeignKey(Complains, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Responses"

    # def __str__(self):
    #     return self.complains + ' ' + self.description
