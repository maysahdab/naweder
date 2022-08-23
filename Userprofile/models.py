from django.db import models
from django.contrib.auth.models import User
from Address.models import Street
# Create your models here.


class UserProfile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile1')
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    guide = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


