from Animal.models import Animal, AnimalFamily, AnimalClass, Animals, Family
from Operation.models import *
from OfferSale.models import *

from rest_framework import serializers


#class FamilySerializer(serializers.ModelSerializer):
    #animalfamily = AnimalFamilySerializer
   # class Meta:
     #   model = Family
     #   fields = ('name', 'namear', 'description', 'descriptionar')


#class AnimalsSerializer(serializers.ModelSerializer):
    #animalclass = AnimalClassSerializer(many=True)
  #  family = FamilySerializer(many=True)

 #   class Meta:
    #    model = Animals
     #   fields = ('animalclass', 'name', 'namear', 'description', 'descriptionar','family')
#

class AnimalClassSerializer(serializers.ModelSerializer):
    Animal= AnimalSerializer(many=True)
    class Meta:
        model = AnimalClass
        fields = ('name', 'namear', 'description', 'descriptionar','Animals')


#lass AnimalFamilySerializer(serializers.ModelSerializer):
  #  animals = AnimalsSerializer
  #  family = FamilySerializer
   # class Meta:
    #    model = AnimalFamily
     #   fields = ('animals', 'family')


class AnimalSerializer(serializers.ModelSerializer):
    #animalfamily = AnimalFamilySerializer(many=True)
    class Meta:
        model = Animal
        fields = ( 'name', 'namear', 'birthdate', 'isactive','animalfamily')
        depth = 1


