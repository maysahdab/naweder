from django.contrib import admin
from .models import *
from Animal.models import *
# Register your models here.
from .models import *


class OperationAdmin(admin.ModelAdmin):
    # fields = ('operationtype','animal', 'operationdate', 'price')
    inlines = (Certificateinline,Picturesinline,Vaccinesinline,)

    # search_fields = ['animal__name',]
    #
    # def get_search_results(self, request, queryset, search_term):
    #     # print("In get search results")
    #     results = super().get_search_results(request, queryset, search_term)
    #     return results
    #
    # def get_queryset(self, request):
    #     qs = super(OperationAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     else:
    #         # myOperations = Operation.objects.filter(user=request.user)
    #         # myAuctions = Auction.objects.filter(operation=myOperations)
    #         # self.fields['animal'].queryset = Animal.objects.filter(user=request.user)
    #         user = request.user
    #         return qs.filter(user=user)
    #
    #         # return qs.filter(user=request.user)


class CertificateTypeAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar')

class VaccineTypeAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar',)

class ReviewOperationAdmin(admin.ModelAdmin):
    fields = ( 'operation', 'user', "rate", 'description', 'descriptionar',)
# class CertificateAdmin(admin.ModelAdmin):
#     fields = ( 'type', 'operation', 'number', 'certificatedate',)
#
# class PicturesAdmin(admin.ModelAdmin):
#     fields = ( 'operation', 'image', )
#
# class VaccinesAdmin(admin.ModelAdmin):
#     fields = ( 'type', 'operation', 'number', 'vaccinedate',)


admin.site.register(Operation, OperationAdmin)
admin.site.register(CertificateType,CertificateTypeAdmin)
admin.site.register(VaccineType,VaccineTypeAdmin)


admin.site.register(ReviewOperation,ReviewOperationAdmin)
admin.site.register(RefundOperation)
admin.site.register(RefundRequestOperation)

admin.site.register(Certificate)
admin.site.register(Pictures)
admin.site.register(Vaccines)
