from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Auction.models import Auction
from Publicity.models import Publicity, ImagePublicity
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from datetime import datetime

from rest_framework import mixins, viewsets


# Create your views here.


class PublicityViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = PublicitySerializer  # shu badu yesta3mel la ye2ra

    # permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    # authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request  # .filter(id=2).all()
        return obj

    def get_queryset(self):
        getData = self.get_object()
        idA = getData.GET['id']

        queryset = Publicity.objects.filter(id=idA)  # (pk=self.kwargs['idA'])
        return queryset


class PublicityimagesViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = ImagePublicitySerializer  # shu badu yesta3mel la ye2ra

    # permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    # authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        idA = getData.GET['id']

        queryset = ImagePublicity.objects.filter(publicity_id=idA)  # (pk=self.kwargs['idA'])
        return queryset


@api_view(['DELETE'])
def Publicity_delete(request, pk):
    try:
        publicity = Publicity.objects.get(pk=pk)
        publicity.delete()
        return JsonResponse({'message': 'The Publicity was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Publicity.DoesNotExist:
        return JsonResponse({'message': 'The Publicity does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def Publicity_add(request):
    try:
        if request.method == 'POST':

            Publ = Publicity.objects.create(user_id=request.data['user'],
                                            description=request.data['description'],
                                            descriptionar=request.data['descriptionar'],
                                            price=request.data['price'],
                                            currency_id=request.data['currency'],
                                            phone=request.data['phone'],
                                            # fromdate=request.data['fromdate'],
                                            # todate=request.data['todate'],
                                            published=request.data['published'],
                                            street_id=request.data['street'],
                                            type_id=request.data['type'],

                                            created_at=datetime.today(),
                                            updated_at=datetime.today()
                                            )

            if eval(request.data['ChangeImage']):
                if request.data.getlist('images') != ['']:
                    for f in request.data.getlist('images'):
                        fs = FileSystemStorage()
                        filename = fs.save(f.name, f)

                        ImagePublicity.objects.create(publicity_id=Publ.id,
                                                      image=f.name,
                                                      created_at=datetime.today(),
                                                      updated_at=datetime.today()
                                                      )
        return JsonResponse({'message': 'Complain is created successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def Publicity_update(request, pk):
    try:
        Publ = Publicity.objects.filter(id=pk).update(user_id=request.data['user'],
                                                      description=request.data['description'],
                                                      descriptionar=request.data['descriptionar'],
                                                      price=request.data['price'],
                                                      currency_id=request.data['currency'],
                                                      phone=request.data['phone'],
                                                      # fromdate=request.data['fromdate'],
                                                      # todate=request.data['todate'],
                                                      published=request.data['published'],
                                                      street_id=request.data['street'],
                                                      type_id=request.data['type'],

                                                      created_at=datetime.today(),
                                                      updated_at=datetime.today()
                                                      )
        if eval(request.data['ChangeImage']):
            ImagePublicity.objects.filter(publicity_id=pk).delete()
            if request.data.getlist('images') != ['']:
                for f in request.data.getlist('images'):
                    fs = FileSystemStorage()
                    filename = fs.save(f.name, f)

                    ImagePublicity.objects.create(publicity_id=pk,
                                                  image=f.name,
                                                  created_at=datetime.today(),
                                                  updated_at=datetime.today()
                                                  )

        return JsonResponse({'message': 'Publicity is updated successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'The Publicity does not exist'}, status=status.HTTP_404_NOT_FOUND)
