from django.contrib import admin
from .models import *

class ComplainsAdmin(admin.ModelAdmin):
    inlines = (ImageComplainsinline,)

admin.site.register(Complains,ComplainsAdmin)
admin.site.register(Response)
# admin.site.register(ImageComplains)

