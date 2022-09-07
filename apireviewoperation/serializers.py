from rest_framework import serializers
# now import models from models.py
# from Ecommerce.models import *
from rest_framework import serializers
from Ecommerce.models import ReviewProduct


# class ReviewProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     userid = serializers.IntegerField()
#     username = serializers.CharField()
#     productid = serializers.IntegerField()
#     productname = serializers.CharField()
#     productnamear = serializers.CharField()
#     rate = serializers.IntegerField()
#     description = serializers.CharField()
#     descriptionar = serializers.CharField()
from Operation.models import ReviewOperation


class ReviewOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewOperation
        fields = ('id', 'operation_id', 'user_id', 'rate', 'description', 'descriptionar')
        # fields = '__all__'
        # depth = 1

