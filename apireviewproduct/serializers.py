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

class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewProduct
        fields = ('id', 'product_id', 'user_id', 'description', 'descriptionar')
        # fields = '__all__'
        depth = 1

