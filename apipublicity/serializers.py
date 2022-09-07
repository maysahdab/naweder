from rest_framework import serializers
# now import models from models.py
# from Complains.models import Complains, ImageComplains, ImageComplainsinline
from currencyapp.models import Currency
from Publicity.models import Service, TypePublicity, ImagePublicity, Publicity
from Address.models import Street

from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', 'description', 'descriptionar')
        # fields = '__all__'
        # depth = 1

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'namear', 'description', 'descriptionar')
        # fields = '__all__'
        # depth = 1

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        # fields = ('id', 'name', 'namear', 'description', 'descriptionar')
        fields = '__all__'
        # depth = 1

class TypePublicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePublicity
        fields = ('id', 'name', 'namear', 'description', 'descriptionar')
        # fields = '__all__'
        # depth = 1

# class ImagePublicitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImagePublicity
#         fields = ('image',)  # 'id', 'publicity_id',


# class PublicitySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     user_id = serializers.IntegerField()
#     description = serializers.CharField()
#     descriptionar = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=1)
#     currency = CurrencySerializer(many=False)
#
#     phone = serializers.CharField()
#     fromdate = serializers.CharField()
#     todate = serializers.DateTimeField()
#     published = serializers.BooleanField()
#     service = ServiceSerializer(many=True)
#     street = StreetSerializer(many=False)
#     type = TypePublicitySerializer(many=False)
#
#     # images = ImagePublicitySerializer(many=True, read_only=True)
#     # rider_image = serializers.SerializerMethodField()
#
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()


class PublicitySerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField()
    currency = CurrencySerializer(many=False)
    service = ServiceSerializer(many=True)
    # street = StreetSerializer(many=False)
    # type = TypePublicitySerializer(many=False)
    # publicity_image = serializers.SerializerMethodField()

    class Meta:
        model = Publicity
        fields = ('id', 'user_id', 'description', 'descriptionar', 'price', 'currency',
                  'phone', 'fromdate', 'todate', 'published', 'service', 'type', 'street',
                  'image_pub') #'ImagePublicity_set',
        depth = 1

    # def get_publicity_image(self, obj):
    #     req = self.context['request']
    #     # build_absolute_uri will convert your related url to absolute url
    #     return req.build_absolute_uri(obj.image.image.url)

