from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from Operation.models import *
from Address.models import *


# Create your models here.
class AuctionStatus(models.Model):
    name = models.CharField(max_length=50, default='')
    namear = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Auction Status"


class Auction(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, blank=True)
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    address = models.CharField(max_length=300, default='')
    fromdate = models.DateField(default=datetime.now)
    todate = models.DateField(default=datetime.now)
    status = models.ForeignKey(AuctionStatus, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    todateextended = models.DateField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    comissionguid = models.FloatField(default=0)
    comissionadmin = models.FloatField(default=0)

    timehourstr = (('00', '00'), ('01', '01'),
                   ('02', '02'), ('03', '03'),
                   ('04', '04'), ('05', '05'),
                   ('06', '06'), ('07', '07'),
                   ('08', '08'), ('09', '09'),
                   ('10', '10'), ('11', '11'),
                   ('12', '12'), ('13', '13'),
                   ('14', '14'), ('15', '15'),
                   ('16', '16'), ('17', '17'),
                   ('18', '18'), ('19', '19'),
                   ('20', '20'), ('21', '21'),
                   ('22', '22'), ('23', '23'),
                   )

    timeminutestr = (('00', '00'), ('15', '15'),
                     ('30', '30'), ('45', '45')
                     )

    fromtimehour = models.CharField(max_length=2, choices=timehourstr, default='08')

    fromtimeminute = models.CharField(max_length=2, choices=timeminutestr, default='00')

    totimehour = models.CharField(max_length=2, choices=timehourstr, default='08')

    totimeminute = models.CharField(max_length=2, choices=timeminutestr, default='00')

    totimeextendedhour = models.CharField(max_length=2, choices=timehourstr, default='', blank=True)

    totimeextendedminute = models.CharField(max_length=2, choices=timeminutestr, default='', blank=True)

    def __str__(self):
        return self.operation.animal.name


class Bids(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.PROTECT, blank=True)
    biddatetime = models.DateTimeField(default=datetime.now, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    subscriber = models.ForeignKey(User, on_delete=models.PROTECT)
    win = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Bids"


class Bidsinline(admin.TabularInline):
    fields = ('auction', 'biddatetime', 'amount', 'subscriber', 'win',)
    model = Bids
    extra = 1
