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


################################################################
@api_view(['POST'])
def Complains_list(request):
    # if request.method == 'GET':
    #     complains = Complains.objects.all()
    #     tutorial_serializer = ComplainsSerializer(complains)
    #     return JsonResponse(tutorial_serializer.data)
    #
    #     # description = request.query_params.get('description', None)
    #     # if description is not None:
    #     #     tutorials = complains.filter(description__icontains=description)
    #     #
    #     # tutorials_serializer = ComplainsSerializer(complains, many=True)
    #     # return JsonResponse(tutorials_serializer.data, safe=False)
    #     # # 'safe=False' for objects serialization

    if request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = ComplainsSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
        #     tutorial_serializer.save()
        #     return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        compl = Complains.objects.create(user_id=request.data['user'], description=request.data['description'])
        # print(eval(request.data['ChangeImage']))

        if eval(request.data['ChangeImage']):
            # ImageComplains.objects.filter(complains_id=pk).delete()
            if request.data.getlist('images') != ['']:
                for f in request.data.getlist('images'):
                    fs = FileSystemStorage()
                    filename = fs.save(f.name, f)
                    print(f.name)
                    ImageComplains.objects.create(complains_id=compl.id,
                                                  image=f.name,
                                                  created_at=datetime.today(),
                                                  updated_at=datetime.today()
                                                  )
        return JsonResponse({'message': 'Complain is created successfully!'}, status=status.HTTP_201_CREATED)


    # elif request.method == 'DELETE':
    #     count = Complains.objects.all().delete()
    #     return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
    #                         status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Complains_detail(request, pk):
    try:
        complains = Complains.objects.get(pk=pk)
    except Complains.DoesNotExist:
        return JsonResponse({'message': 'The complains does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ComplainsSerializer(complains)
        return JsonResponse(tutorial_serializer.data)

    # elif request.method == 'PUT':
    #     data = request.data
    #     # myfile = request.FILES['images']
    #     # print(request)
    #     # print(request.FILES)
    #     # request.FILES["images"]
    #     # fs = FileSystemStorage()
    #     # filename = fs.save(myfile.name, myfile)
    #     #
    #     # print(fs.url(filename))
    #
    #     # compl = Complains.objects.get(id=pk).update(user_id=data['id'], description=data['description'],
    #     # image = request.FILES["images"])
    #
    #     myfile = request.FILES.getlist('images')
    #
    #     compl = Complains.objects.filter(id=pk).update(user_id=data['user'], description=data['description'])
    #     # print(request.FILES)
    #     print(myfile)
    #     # print(request.data["images"][1])
    #     # print(request.data)
    #     fs = FileSystemStorage()
    #     # filename = fs.save(request.FILES["images"][0].name, request.FILES["images"][0])
    #     # for img in request.FILES["images"]:
    #     #
    #     #     fs = FileSystemStorage()
    #     #     filename = fs.save(img.name, img)
    #     #
    #     #     print(fs.url(filename))
    #
    #     return JsonResponse()
    #     # if tutorial_serializer.is_valid():
    #     #     tutorial_serializer.save()
    #     #     return JsonResponse(tutorial_serializer.data)
    #     # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        compl = Complains.objects.filter(id=pk).update(user_id=request.data['user'], description=request.data['description'])
        # print(eval(request.data['ChangeImage']))

        if eval(request.data['ChangeImage']):
            ImageComplains.objects.filter(complains_id=pk).delete()
            if request.data.getlist('images') != ['']:
                for f in request.data.getlist('images'):
                    fs = FileSystemStorage()
                    filename = fs.save(f.name, f)
                    print(f.name)
                    ImageComplains.objects.create(complains_id=pk,
                                                  image=f.name,
                                                  created_at=datetime.today(),
                                                  updated_at=datetime.today()
                                                  )

        # response = {"result": 'User Profile Updated'}
        # return Response(response)
        return JsonResponse({'message': 'Complain is updated successfully!'}, status=status.HTTP_200_OK)
        # if tutorial_serializer.is_valid():
        #     # tutorial_serializer.save()
        #     return JsonResponse(tutorial_serializer.data)
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        complains.delete()
        return JsonResponse({'message': 'ٌRoom Type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class ImageComplainsViews(viewsets.ModelViewSet):
    queryset = ImageComplains.objects.all()
    serializer_class = ImageComplainsSerializer

def getComplainbyid(id):
    sql = " SELECT Complains_Complains.id, Complains_Complains.description, Complains_ImageComplains.image  " \
          " FROM  Complains_Complains " \
          " INNER JOIN Complains_ImageComplains on Complains_ImageComplains.complains_id = Complains_Complains.id" \
          " where Complains_Complains.id =" + str(id)

    complainlist = []
    complainslistimage = []
    row = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()

    sqlimages = " SELECT Complains_ImageComplains.image" \
                " FROM  Complains_ImageComplains" \
                " where Complains_ImageComplains.complains_id =" + str(id)

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
    sqlimages = " SELECT Complains_ImageComplains.image" \
                " FROM  Complains_ImageComplains" \
                " where Complains_ImageComplains.complains_id = " + str(complains_id)

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

def getAllComplainsImages():
    sql = " SELECT Complains_Complains.id, Complains_Complains.description  " \
          " FROM Complains_Complains "

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

        queryset = getAllComplainsImages()
        return queryset
