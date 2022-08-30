from rest_framework import serializers
# now import models from models.py
from Complains.models import Complains, ImageComplains, ImageComplainsinline
from rest_framework import serializers


class ImageComplainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComplains
        fields = ('id', 'image', 'complains',)
        # fields = '__all__'
        depth = 1


class ComplainsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # user_id = serializers.IntegerField()
    description = serializers.CharField()
    images = serializers.ListField()

# class Complains2Serializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     # user_id = serializers.IntegerField()
#     description = serializers.CharField()
#     # images = serializers.ListField()
