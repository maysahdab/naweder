from rest_framework import serializers
# now import models from models.py
from rest_framework import serializers

from Ecommerce.models import Product

# class AnimalSerializer4(serializers.ModelSerializer):
#     class Meta:
#         model = Animal
#         fields = ('id', 'animalclass_id', 'name', 'namear', 'birthdate', 'isactive')
#         # fields = '__all__'
#         depth = 1
#
# class OperationAnimalSerializer(serializers.ModelSerializer):
#     animal = AnimalSerializer4(many=False)
#     class Meta:
#         model = Operation
#         fields = ('id', 'animal', )
#         # fields = '__all__'
#         depth = 1
from Ecommerce.models import Tag


class EcomProductSerializer(serializers.ModelSerializer):
    # currency = Serializer(many=False)
    class Meta:
        # ordering = ['-id']
        model = Product
        fields = ('id', 'name', 'description', 'descriptionar', 'sku', 'slug', 'quantity', 'startat', 'endat',
                  'publishedat', 'price', 'currency', 'discount', 'percentage', 'productcategory', 'tag',
                  'productalternative', 'productcomlementary', 'created_at', 'updated_at',
                  )
        # fields = '__all__'
        # extra_kwargs = {'name': {'required': False}}
        depth = 1

###############################################################

# class tagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ['id',]


class EcomProductSerializer2(serializers.ModelSerializer):
    # tag = tagSerializer(many=True)
    class Meta:
        # ordering = ['-id']
        model = Product
        fields = ('id', 'name', 'description', 'descriptionar', 'sku', 'slug', 'quantity', 'startat', 'endat',
                  'publishedat', 'price', 'currency', 'discount', 'percentage', 'productcategory',
                  'tag', 'productalternative', 'productcomlementary', 'created_at', 'updated_at',
                  #
                  )
        # fields = '__all__'
        # extra_kwargs = {'name': {'required': False}}
        depth = 1

    # def update(self, instance, validated_data):
    #     tag_list = validated_data.get('tag')
    #     instance.tag.clear()
    #     for i in tag_list:
    #         tag = i.get('id')
    #         product = Product.objects.get(id=tag)
    #         if product != None :
    #             instance.mentor.add(product)
    #     return instance
