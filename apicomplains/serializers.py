from rest_framework import serializers
# now import models from models.py
from Complains.models import Complains, ImageComplains, ImageComplainsinline
from rest_framework import serializers


# class ComplainsSerializer(serializers.ModelSerializer):
#     # commenter_name = serializers.CharField(source='usr.username', read_only=True)
#     # created_time = serializer.DateTimeField(read_only=True, required=False)
#
#     # cover_image = serializers.ImageField(required=False)
#     # type_name = serializers.CharField(required=False)
#     # type_name_ar = serializers.CharField(required=False)
#     ##area = serializers.IntegerField(required=False)
#     # bedType = serializers.CharField(required=False)
#     # bedType_ar = serializers.CharField(required=False)
#     ##capacity = serializers.IntegerField(required=False)
#     ##price_per_day = serializers.IntegerField(required=False)
#     # user = serializers.IntegerField()
#
#     # description = serializers.CharField()
#     # image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True,
#     #                                      required=False)
#     class Meta:
#         model = Complains
#         fields = ('id', 'user', 'description', )
#         # fields = '__all__'


class ImageComplainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComplains
        fields = ('id', 'imageText', 'complains',)
        # fields = '__all__'
        depth = 1


class ComplainsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # user_id = serializers.IntegerField()
    description = serializers.CharField()
    images = serializers.ListField()


# class ComplainsSerializer(serializers.ModelSerializer):
#     # movie = MovieSerializer(read_only=True)
#     # movieId = serializers.PrimaryKeyRelatedField(write_only=True,
#     #                                              queryset=Movie.objects.all(),
#     #                                              source='movie')
#     images = ImageComplainsSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Complains
#         fields = ['user_id', 'description', 'images', 'created_at', 'updated_at']

# class ImageComplainsSerializer(serializers.ModelSerializer):
#     Complains = ComplainsSerializer(read_only=True)
#     ComplainId = serializers.PrimaryKeyRelatedField(write_only=True,
#                                                     queryset=Complains.objects.all(),
#                                                     source='complains')
#     # schedule = serializers.SerializerMethodField()
#
#
#     class Meta:
#         model = ImageComplains
#         fields = ['Complains', 'ComplainId', 'imageText', 'created_at', 'updated_at']
#         depth = 1



