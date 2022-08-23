from django.db import models

class SystemSetting(models.Model):
    tva = models.DecimalField(default=0, decimal_places=1, max_digits=2)
