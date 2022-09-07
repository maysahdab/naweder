from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from Ecommerce.models import ReviewProduct
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime
# Create your views here.
from Operation.models import ReviewOperation


class MyOperationReviewsViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = ReviewOperationSerializer  # shu badu yesta3mel la ye2ra
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        # idA = getData.GET['id']

        queryset = ReviewOperation.objects.filter(user_id=self.request.user.pk)
        return queryset
