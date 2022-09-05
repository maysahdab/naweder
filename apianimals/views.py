from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from Animal.models import *
from Operation.models import Operation

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime
from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


@api_view(['POST'])
def Animal_add(request):
    try:
        if request.method == 'POST':
            pass
        #     compl = Complains.objects.create(user_id=request.data['user'],
        #                                      description=request.data['description'],
        #                                      created_at=datetime.today(),
        #                                      updated_at=datetime.today()
        #                                      )
        #
        #     if eval(request.data['ChangeImage']):
        #         if request.data.getlist('images') != ['']:
        #             for f in request.data.getlist('images'):
        #                 fs = FileSystemStorage()
        #                 filename = fs.save(f.name, f)
        #
        #                 ImageComplains.objects.create(complains_id=compl.id,
        #                                               image=f.name,
        #                                               created_at=datetime.today(),
        #                                               updated_at=datetime.today()
        #                                               )
        # return JsonResponse({'message': 'Animals added for sales'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def MyAnimals(request):
    #try:
    if request.method == 'GET':
        # try:
        oper = Operation.objects.filter(operationtype='Auction')
        print('helo')
        print(oper)
        print(oper.count())

        for i in range(oper.count()):
            print(i)
            animal = oper[i].animal
            animal_serializer = AnimalSerializer(animal)
            return JsonResponse(animal_serializer.data)
        #
        # except :
            #     return JsonResponse({'message': 'do not have an animals'}, status=status.HTTP_404_NOT_FOUND)
    # except:
    #     return JsonResponse({'message': 'Error'}, status=status.HTTP_404_NOT_FOUND)


class AnimalclassViews(viewsets.ModelViewSet):
    queryset = AnimalClass.objects.all()
    #permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = AnimalClassSerializer


class AnimalsViews(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    #permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = AnimalsSerializer


class FamilyViews(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    #permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = FamilySerializer


class AnimalViews(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    #permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = AnimalSerializer


class AnimalFamilyViews(viewsets.ModelViewSet):
    queryset = AnimalFamily.objects.all()
    #permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = AnimalFamilySerializer


