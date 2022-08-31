from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Auction.models import Auction

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime, date
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class AuctionViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = ActionSerializer  # shu badu yesta3mel la ye2ra

    def get_queryset(self):
        return Auction.objects.all().filter(todate=date.today()).all()
