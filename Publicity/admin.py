from django.contrib import admin
from .models import *


class PublicityAdmin(admin.ModelAdmin):
    inlines = (PublicityService_Inline,ImagePublicitysinline,)


admin.site.register(Publicity, PublicityAdmin)
admin.site.register(Service)
#admin.site.register(ImagePublicity)
admin.site.register(TypePublicity)

