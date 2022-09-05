from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Complains.models import Complains, Response, ImageComplains, ImageComplainsinline

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['POST'])
def Complain_add(request):

    try:
        if request.method == 'POST':

            compl = Complains.objects.create(user_id=request.data['user'],
                                             description=request.data['description'],
                                             created_at=datetime.today(),
                                             updated_at=datetime.today()
                                             )


            if eval(request.data['ChangeImage']):
                if request.data.getlist('images') != ['']:
                    for f in request.data.getlist('images'):
                        fs = FileSystemStorage()
                        filename = fs.save(f.name, f)

                        ImageComplains.objects.create(complains_id=compl.id,
                                                      image=f.name,
                                                      created_at=datetime.today(),
                                                      updated_at=datetime.today()
                                                      )
        return JsonResponse({'message': 'Complain is created successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def Complain_delete(request, pk):
    try:
        complains = Complains.objects.get(pk=pk)
        complains.delete()
        return JsonResponse({'message':'The Complain was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Complains.DoesNotExist:
        return JsonResponse({'message': 'The complain does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def Complain_update(request, pk):
    try:
        compl = Complains.objects.filter(id=pk).update(user_id=request.data['user'],
                                                       description=request.data['description'],
                                                       created_at=datetime.today(),
                                                       updated_at=datetime.today()
                                                       )
        if eval(request.data['ChangeImage']):
            ImageComplains.objects.filter(complains_id=pk).delete()
            if request.data.getlist('images') != ['']:
                for f in request.data.getlist('images'):
                    fs = FileSystemStorage()
                    filename = fs.save(f.name, f)

                    ImageComplains.objects.create(complains_id=pk,
                                                  image=f.name,
                                                  created_at=datetime.today(),
                                                  updated_at=datetime.today()
                                                  )

        return JsonResponse({'message': 'Complain is updated successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'The complain does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def Complains_detail(request, pk):
    try:
        complains = Complains.objects.get(pk=pk)


    except Complains.DoesNotExist:
        return JsonResponse({'message': 'The complains does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ComplainsSerializer(complains)
        return JsonResponse(tutorial_serializer.data)


    # elif request.method == 'PUT':
    #     compl = Complains.objects.filter(id=pk).update(user_id=request.data['user'], description=request.data['description'])
    #     # print(eval(request.data['ChangeImage']))
    #
    #     if eval(request.data['ChangeImage']):
    #         ImageComplains.objects.filter(complains_id=pk).delete()
    #         if request.data.getlist('images') != ['']:
    #             for f in request.data.getlist('images'):
    #                 fs = FileSystemStorage()
    #                 filename = fs.save(f.name, f)
    #                 print(f.name)
    #                 ImageComplains.objects.create(complains_id=pk,
    #                                               image=f.name,
    #                                               created_at=datetime.today(),
    #                                               updated_at=datetime.today()
    #                                               )
    #
    #
    #     return JsonResponse({'message': 'Complain is updated successfully!'}, status=status.HTTP_200_OK)


class ImageComplainsViews(viewsets.ModelViewSet):
    queryset = ImageComplains.objects.all()
    serializer_class = ImageComplainsSerializer


def getComplainbyid(id):
    sql = " SELECT Complains_complains.id, Complains_complains.description, Complains_imagecomplains.image  " \
          " FROM  Complains_complains " \
          " INNER JOIN Complains_imagecomplains on Complains_imagecomplains.complains_id = Complains_complains.id" \
          " where Complains_complains.id =" + str(id)

    complainlist = []
    complainslistimage = []
    row = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()


    if row== None:

        return complainlist

    sqlimages = " SELECT Complains_imagecomplains.image" \
                " FROM  Complains_imagecomplains" \
                " where Complains_imagecomplains.complains_id =" + str(id)

    with connection.cursor() as cursor:
        cursor.execute(sqlimages)
        rows = cursor.fetchall()

        for rowim in rows:
            if rowim[0]:
                imagepath = "media/" + str(rowim[0])
            else:
                imagepath = ""
            roomimage = {
                'images': imagepath
            }

            complainslistimage.append(roomimage)

    complain1 = {
        'id': row[0],
        'description': row[1],
        'images': complainslistimage,
        }

    complainlist.append(complain1)



    return complainlist


def getComplainsImages(complains_id):
    sqlimages = " SELECT Complains_imagecomplains.image" \
                " FROM  Complains_imagecomplains" \
                " where Complains_imagecomplains.complains_id = " + str(complains_id)

    complainslistimage = []
    row = []



    with connection.cursor() as cursor:
        cursor.execute(sqlimages)
        rows = cursor.fetchall()

        for rowim in rows:
            imagepath = "media/" + str(rowim[0])
            roomimage = {
                'images': imagepath
            }
            complainslistimage.append(roomimage)

    return complainslistimage


def getAllComplainsWithImages():
    sql = " SELECT Complains_complains.id, Complains_complains.description  " \
          " FROM Complains_complains "

    complainlist = []
    complainslistimage = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            complain1 = {
                'id': row[0],
                'description': row[1],
                'images': getComplainsImages(row[0]),
                }

            complainlist.append(complain1)

    return complainlist

def getComplainbyUserid(userid):
    sql = "SELECT Complains_complains.id, Complains_complains.description "\
          " FROM  Complains_complains"\
          " where Complains_complains.user_id =" + str(userid) #str(self.request.user.pk)

    complainlist = []
    complainslistimage = []
    rows = []
    rowsimg = []
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows is None:
            return complainlist
        for row in rows:

            sqlimages = " SELECT Complains_imagecomplains.image" \
                        " FROM Complains_imagecomplains" \
                        " where Complains_imagecomplains.complains_id =" + str(row[0])
            with connection.cursor() as cursor:
                cursor.execute(sqlimages)
                rowsimg = cursor.fetchall()
            complainslistimage = []
            for rowi in rowsimg:
                if rowi[0]:
                    imagepath = "media/" + str(rowi[0])
                else:
                    imagepath = ""
                roomimage = {
                    'images': imagepath
                }

                complainslistimage.append(roomimage)

            complain1 = {
                'id': row[0],
                'description': row[1],
                'images': complainslistimage,
                }
            complainlist.append(complain1)

    return complainlist


class ComplainsViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ComplainsSerializer

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

        queryset = getComplainbyid(id)

        return queryset


class AllComplainsViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ComplainsSerializer

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

        queryset = getAllComplainsWithImages()
        return queryset

# class MyComplainsViews(mixins.ListModelMixin, viewsets.GenericViewSet):
#     serializer_class = Complains2Serializer
#     permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
#     authentication_classes = [JWTAuthentication]  # this will handel authentication automatically
#
#     def get_object(self, queryset=None):
#         obj = self.request
#         return obj
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         # getData = self.get_object()
#         # # id = getData.GET['id']
#         #
#         # queryset = getAllComplainsWithImages()
#         # return queryset
#
#         # return getComplainbyUserid(self.request.user.pk)
#         return Complains.objects.all().filter(user_id=self.request.user.pk).all()


class MyComplainsViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ComplainsSerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

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

        queryset = getComplainbyUserid(self.request.user.pk)
        return queryset
        # return Complains.objects.all().filter(user_id=self.request.user.pk).all()

# class myComplainsViews(viewsets.ModelViewSet):
#     queryset = Complains.objects.all()  # mn ayy table badi jibon
#     serializer_class = ComplainsSerializer  # shu badu yesta3mel la ye2ra
#     permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
#     authentication_classes = [JWTAuthentication]  # this will handel authentication automatically
#
#     def get_queryset(self):
#         return Complains.objects.all().filter(usr_id=self.request.user.pk).all()
