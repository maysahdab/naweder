from rest_framework import serializers
# now import models from models.py
from rest_framework import serializers

from Auction.models import Auction, AuctionStatus
from Animal.models import Animal, Family, AnimalClass
from Operation.models import Operation


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionStatus
        fields = ('id', 'name', 'namear', 'created_at', 'updated_at',)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'namear', 'birthdate',)


class OperationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)

    class Meta:
        model = Operation
        fields = ('id', 'animal', 'price',)


class AuctionSerializer(serializers.ModelSerializer):
    # commenter_name = serializers.CharField(source='usr.username', read_only=True)
    operation = OperationSerializer(read_only=True)
    # street = serializers.CharField(source='usr.username', read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = ('id', 'fromdate', 'todate', 'description', 'descriptionar', 'status', 'operation',)

#############################################################


class AnimalFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'name', 'namear', 'description', 'descriptionar',)

class AnimalClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClass
        fields = ('id', 'name', 'namear', 'description', 'descriptionar',)

class AnimalSerializer2(serializers.ModelSerializer):
    family = AnimalFamilySerializer(read_only=True)
    # animalclass = AnimalClassSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = ('id', 'name', 'namear', 'birthdate', 'family', )

###############################################################

