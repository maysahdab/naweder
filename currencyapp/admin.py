from django.contrib import admin
from .models import *
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'symbol','description', 'descriptionar',)
admin.site.register(Currency,CurrencyAdmin)


# class SystemSettingsAdmin(admin.ModelAdmin):
#   def has_add_permission(self, request):
#     # if there's already an entry, do not allow adding
#     count = SystemSettings.objects.all().count()
#     if count == 0:
#       return True
#
#     return False
#
# admin.site.register(SystemSettings,SystemSettingsAdmin)
