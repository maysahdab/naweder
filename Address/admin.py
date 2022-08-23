from django.contrib import admin
from .models import *

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar',)

class ProvinceAdmin(admin.ModelAdmin):
    fields = ( 'country','name', 'namear', 'description', 'descriptionar',)

class CityAdmin(admin.ModelAdmin):
    fields = ( 'province','name', 'namear', 'description', 'descriptionar',)

class RegionAdmin(admin.ModelAdmin):
    fields = ( 'city','name', 'namear', 'description', 'descriptionar',)

class StreetAdmin(admin.ModelAdmin):
    fields = ( 'region','name', 'namear', 'description', 'descriptionar',)

admin.site.register(Country,CountryAdmin)
admin.site.register(Province,ProvinceAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Street,StreetAdmin)

