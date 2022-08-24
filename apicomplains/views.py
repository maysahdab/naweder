from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from Complains.models import Complains, Response, ImageComplains, ImageComplainsinline

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage


################################################################

class ImageComplainsViews(viewsets.ModelViewSet):
    queryset = ImageComplains.objects.all()
    serializer_class = ImageComplainsSerializer


@api_view(['GET', 'POST', 'DELETE'])
def Complains_list(request):
    if request.method == 'GET':
        complains = Complains.objects.all()

        description = request.query_params.get('description', None)
        if description is not None:
            tutorials = complains.filter(description__icontains=description)

        tutorials_serializer = ComplainsSerializer(complains, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ComplainsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Complains.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Complains_detail(request, pk):
    try:
        complains = Complains.objects.get(pk=pk)
    except Complains.DoesNotExist:
        return JsonResponse({'message': 'The complains does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = ComplainsSerializer(complains)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':

        data = request.data

        myfile = request.FILES['images']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        print(fs.url(filename))

        # compl = Complains.objects.get(id=pk).update(user_id=data['id'], description=data['description'],image = request.FILES["images"])

        compl = Complains.objects.filter(id=pk).update(user_id=data['user'], description=data['description'],
                                                       image=request.FILES["images"])

        print('okkkkkkkkkkkkkkk')

        # tutorial_serializer = ComplainsSerializer(complains, data=data)

        response = {"result": 'User Profile Updated'}

        print(response)
        return Response(response)

        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        complains.delete()
        return JsonResponse({'message': 'ٌRoom Type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
