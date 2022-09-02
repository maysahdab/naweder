from django.contrib import admin
from .models import *

# Register your models here.


# admin.site.register(AnimalClass)
# admin.site.register(Animals)
# admin.site.register(Animal)


class AnimalsAdmin(admin.ModelAdmin):
    fields = ('animalclass', 'name', 'namear', 'description', 'descriptionar',)
    inlines = (AnimalFamily_Inline,)

class FamilyAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar',)

class AnimalClassAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar',)

class AnimalAdmin(admin.ModelAdmin):
    # fields =('family','name','namear','birthdate','isactive',)
    def get_queryset(self, request):

        qs = super(AnimalAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            # myOperations = Operation.objects.filter(user=request.user)
            # myAuctions = Auction.objects.filter(operation=myOperations)

            return qs.filter(user=request.user)

admin.site.register(Animals, AnimalsAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Family,FamilyAdmin)
admin.site.register(AnimalClass,AnimalClassAdmin)