from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Auction.models import Auction
from Animal.models import Animal
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime, date
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class AuctionEndTodayViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = AuctionSerializer  # shu badu yesta3mel la ye2ra

    def get_queryset(self):
        return Auction.objects.all().filter(todate=date.today()).all()


# class AuctionByIdViews(APIView):
#     # queryset = Review.objects.all()  # mn ayy table badi jibon
#     serializer_class = AuctionSerializer  # shu badu yesta3mel la ye2ra
#
#     def get_queryset(self):
#         auctions = Auction.objects.all()  # .filter(id=id).all()
#         print("!!!!!!!!!")
#         return auctions
#
#     def get(self, request, *args, **kwargs):
#         try:
#             id = request.query_params["id"]
#             print(id)
#             if id != None:
#                 auction = Auction.objects.get(id=id)
#                 serializer = AuctionSerializer(auction)
#         except:
#             auctions = self.get_queryset()
#             serializer = AuctionSerializer(auctions, many=True)
#
#         return Response(serializer.data)

# class AuctionByIdViews(generics.ListCreateAPIView):
#     # queryset = Review.objects.all()  # mn ayy table badi jibon
#     serializer_class = AuctionSerializer  # shu badu yesta3mel la ye2ra
#
#     def get_queryset(self):
#         # auctions = Auction.objects.all()  # .filter(id=id).all()
#         # print("!!!!!!!!!")
#         # return auctions
#         queryset = Auction.objects.all() #.filter(pk=self.kwargs['post_id'])
#         return queryset


class LastAddedAuctionViews(generics.ListCreateAPIView):
    serializer_class = AuctionSerializer  # shu badu yesta3mel la ye2ra

    def get_queryset(self):
        queryset = Auction.objects.order_by('-id')[:2]
        return queryset


class AuctionByIdViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AuctionSerializer
    # permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    # authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request  # .filter(id=2).all()
        return obj

    def get_queryset(self):
        getData = self.get_object()
        idA = getData.GET['id']

        queryset = Auction.objects.filter(id=idA)  # (pk=self.kwargs['idA'])
        return queryset
        # return Complains.objects.all().filter(user_id=self.request.user.pk).all()


class AnimalViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = AnimalSerializer2  # shu badu yesta3mel la ye2ra

    def get_queryset(self):
        return Animal.objects.all()


# @api_view(['GET'])
# def AuctionByIdViews(request, pk):
#     try:
#         print(pk)
#         complains = Auction.objects.filter(id=int(pk))
#         print(complains)
#     except:
#         return JsonResponse({'message': 'The Auction does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         tutorial_serializer = AuctionSerializer
#         return JsonResponse(tutorial_serializer.data)
