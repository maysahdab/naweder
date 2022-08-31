from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from Ecommerce.models import *

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime

################################################################


@api_view(['POST'])
def ReviewProduct_add(request):


    if request.method == 'POST':

        reviewproduct = ReviewProduct.objects.create(product_id = request.data['product'],
                                                     user_id=request.data['user'],
                                                     rate = request.data['rate'],
                                                     description = request.data['description'],
                                                     descriptionar=request.data['descriptionar'],
                                                     created_at = datetime.today(),
                                                     updated_at = datetime.today()
                                                    )

        return JsonResponse({'message': 'Review Product is created successfully!'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def ReviewProduct_delete(request, pk):
    try:
        reviewproduct = ReviewProduct.objects.get(pk=pk)
        reviewproduct.delete()
        return JsonResponse({'message':'The review of product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Complains.DoesNotExist:
        return JsonResponse({'message': 'The review of product does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def ReviewProduct_update(request, pk):
    try:
        reviewproduct = ReviewProduct.objects.filter(id=pk).update(product_id = request.data['product'],
                                                     user_id=request.data['user'],
                                                     rate = request.data['rate'],
                                                     description = request.data['description'],
                                                     descriptionar=request.data['descriptionar'],
                                                     created_at = datetime.today(),
                                                     updated_at = datetime.today()
                                                    )


        return JsonResponse({'message': 'The review of product is updated successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'The review of product does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT'])
def ReviewProduct_detail(request, pk):
    try:
        reviewproduct = ReviewProduct.objects.get(pk=pk)


    except ReviewProduct.DoesNotExist:
        return JsonResponse({'message': 'The review of product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ReviewProductSerializer(complains)
        return JsonResponse(tutorial_serializer.data)


def getReviewProductbyid(id):
    sql = " SELECT Ecommerce_reviewproduct.id,auth_user.id as userid, auth_user.username,Ecommerce_product.id as productid, Ecommerce_product.name,Ecommerce_product.namear,  " \
          " Ecommerce_reviewproduct.rate,Ecommerce_reviewproduct.description,Ecommerce_reviewproduct.descriptionar FROM  Ecommerce_reviewproduct " \
          " INNER JOIN auth_user on auth_user.id = Ecommerce_reviewproduct.user_id" \
          " INNER JOIN Ecommerce_product on Ecommerce_product.id = Ecommerce_reviewproduct.product_id" \
          " where Ecommerce_reviewproduct.id =" + str(id)

    complainlist = []

    row = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()


    if row== None:

        return complainlist


    complain1 = {
        'id': row[0],
        'userid': row[1],
        'username': row[2],
        'productid': row[3],
        'productname':row[4],
        'productnamear':row[5],
        'rate':row[6],
        'description':row[7],
        'descriptionar':row[8],

        }

    complainlist.append(complain1)



    return complainlist


class ReviewProductViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReviewProductSerializer

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        getData = self.get_object()
        id = getData.GET['id']

        queryset = getReviewProductbyid(id)

        return queryset



def getAllReviewProduct():
    sql = " SELECT Ecommerce_reviewproduct.id,auth_user.id as userid, auth_user.username,Ecommerce_product.id as productid, Ecommerce_product.name,Ecommerce_product.namear,  " \
          " Ecommerce_reviewproduct.rate,Ecommerce_reviewproduct.description,Ecommerce_reviewproduct.descriptionar FROM  Ecommerce_reviewproduct " \
          " INNER JOIN auth_user on auth_user.id = Ecommerce_reviewproduct.user_id" \
          " INNER JOIN Ecommerce_product on Ecommerce_product.id = Ecommerce_reviewproduct.product_id"

    complainlist = []

    rows = []
    print (sql)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()


    if rows== None:

        return complainlist

    for row in rows:
        complain1 = {
            'id': row[0],
            'userid': row[1],
            'username': row[2],
            'productid': row[3],
            'productname':row[4],
            'productnamear':row[5],
            'rate':row[6],
            'description':row[7],
            'descriptionar':row[8],

            }

        complainlist.append(complain1)



    return complainlist


class AllReviewProductViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReviewProductSerializer

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        getData = self.get_object()
        # id = getData.GET['id']

        queryset = getAllReviewProduct()
        return queryset
