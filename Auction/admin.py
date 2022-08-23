from django.contrib import admin
from .models import *
# Register your models here.
# from Operation.models import Operation

# admin.site.register(Auction)

class AuctionStatusAdmin(admin.ModelAdmin):
    fields = ( 'name', 'namear', 'description', 'descriptionar',)

class AuctionAdmin(admin.ModelAdmin):
    inlines = (Bidsinline,)
    fields = ( 'operation','street','address', 'fromdate','fromtimehour','fromtimeminute', 'todate','totimehour','totimeminute','status', 'description', 'descriptionar','todateextended','totimeextendedhour','totimeextendedminute')
    def get_queryset(self, request):
        qs = super(AuctionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            # myOperations = Operation.objects.filter(user=request.user)
            # myAuctions = Auction.objects.filter(operation=myOperations)

            return qs.filter(operation__user=request.user)


admin.site.register(AuctionStatus,AuctionStatusAdmin)
admin.site.register(Auction, AuctionAdmin)
# admin.site.register(Bids)
