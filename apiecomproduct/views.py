from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from Ecommerce.models import Product
from rest_framework.decorators import api_view
from datetime import datetime
from django.db import models
from rest_framework.response import Response

from rest_framework.templatetags.rest_framework import data

from .serializers import *
from Ecommerce.models import Tag


# Create your views here.


class EcomProductGetByidViews(viewsets.ReadOnlyModelViewSet):
    # queryset = Review.objects.all()  # mn ayy table badi jibon
    serializer_class = EcomProductSerializer  # shu badu yesta3mel la ye2ra

    # permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    # authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        idA = getData.GET['id']

        queryset = Product.objects.filter(id=idA)
        return queryset


@api_view(['DELETE'])
def EcomProduct_delete(request, pk):
    try:
        reviewproduct = Product.objects.get(pk=pk)
        reviewproduct.delete()
        return JsonResponse({'message': 'The product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def ReviewProduct_add(request):
    if request.method == 'POST':
        new_product = Product.objects.create(name=request.data['name'],
                                             namear=request.data['namear'],
                                             # rate=request.data['rate'],
                                             description=request.data['description'],
                                             descriptionar=request.data['descriptionar'],
                                             sku=request.data['sku'],
                                             slug=request.data['slug'],
                                             quantity=request.data['quantity'],
                                             startat=request.data['startat'],
                                             endat=request.data['endat'],
                                             publishedat=request.data['publishedat'],
                                             price=request.data['price'],
                                             currency_id=request.data['currency'],
                                             discount=request.data['discount'],
                                             percentage=request.data['percentage'],
                                             productcategory_id=request.data['productcategory'],
                                             # tag_id=request.data['tag'],
                                             # productalternative_id=request.data['productalternative'],
                                             # productcomlementary_id=request.data['productcomlementary'],

                                             created_at=datetime.today(),
                                             updated_at=datetime.today()
                                             )
        new_product.save()
        for tag in data['tag']:
            tag_obj = models.Tag.objects.get(id=tag['id'])
            new_product.authors.add(tag_obj)

        # for gen in data['genre']:
        #     gen_obj = models.Genre.objects.get(name=gen['name'])
        #     new_Product.genre.add(gen_obj)

        serializer = serializers.EcomProductSerializer(new_product)
        return Response(serializer.data)

        # return JsonResponse({'message': 'Review Product is created successfully!'}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def ReviewProduct_update(request, pk):
    try:
        reviewproduct = Product.objects.filter(id=pk).update(name=request.data['name'],
                                                             namear=request.data['namear'],
                                                             # rate=request.data['rate'],
                                                             description=request.data['description'],
                                                             descriptionar=request.data['descriptionar'],
                                                             sku=request.data['sku'],
                                                             slug=request.data['slug'],
                                                             quantity=request.data['quantity'],
                                                             startat=request.data['startat'],
                                                             endat=request.data['endat'],
                                                             publishedat=request.data['publishedat'],
                                                             price=request.data['price'],
                                                             currency_id=request.data['currency'],
                                                             discount=request.data['discount'],
                                                             percentage=request.data['percentage'],
                                                             productcategory_id=request.data['productcategory'],
                                                             # tag_id=request.data['tag'],
                                                             # productalternative_id=request.data['productalternative'],
                                                             # productcomlementary_id=request.data['productcomlementary'],

                                                             created_at=datetime.today(),
                                                             updated_at=datetime.today()
                                                             )

        return JsonResponse({'message': 'The review of product is updated successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'The review of product does not exist'}, status=status.HTTP_404_NOT_FOUND)
