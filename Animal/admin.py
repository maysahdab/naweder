from django.contrib import admin
from .models import *


class AnimalsAdmin(admin.ModelAdmin):
    fields = ('animalclass', 'name', 'namear', 'description', 'descriptionar',)
    inlines = (AnimalFamily_Inline,)


class FamilyAdmin(admin.ModelAdmin):
    fields = ('name', 'namear', 'description', 'descriptionar',)


class AnimalClassAdmin(admin.ModelAdmin):
    fields = ('name', 'namear', 'description', 'descriptionar',)


class AnimalAdmin(admin.ModelAdmin):
    fields = ('animalclass','name', 'namear', 'birthdate', 'isactive',)

    # def get_queryset(self, request):
    #
    #     qs = super(AnimalAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     else:
    #
    #         return qs.filter(user=request.user)


admin.site.register(AnimalClass,AnimalClassAdmin)
# admin.site.register(Family,FamilyAdmin)
# admin.site.register(Animals, AnimalsAdmin)
admin.site.register(Animal, AnimalAdmin)
# admin.site.register(AnimalFamily)
