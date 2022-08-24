from rest_framework import serializers
# now import models from models.py
from Complains.models import Complains, ImageComplains, ImageComplainsinline
from rest_framework import serializers


class ImageComplainsSerializer(serializers.ModelSerializer):
    model = ImageComplains
    fields = '__all__'


class ComplainsSerializer(serializers.ModelSerializer):
    # commenter_name = serializers.CharField(source='usr.username', read_only=True)
    # created_time = serializer.DateTimeField(read_only=True, required=False)

    # cover_image = serializers.ImageField(required=False)
    # type_name = serializers.CharField(required=False)
    # type_name_ar = serializers.CharField(required=False)
    ##area = serializers.IntegerField(required=False)
    # bedType = serializers.CharField(required=False)
    # bedType_ar = serializers.CharField(required=False)
    ##capacity = serializers.IntegerField(required=False)
    ##price_per_day = serializers.IntegerField(required=False)
    # user = serializers.IntegerField()

    # description = serializers.CharField()
    # image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True,
    #                                      required=False)

    class Meta:
        model = Complains
        fields = ('id', 'user', 'description', )
        # fields = '__all__'
