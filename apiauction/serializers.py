from rest_framework import serializers
# now import models from models.py
from rest_framework import serializers

from Auction.models import Auction, AuctionStatus
from Animal.models import Animal
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


class ActionSerializer(serializers.ModelSerializer):
    # commenter_name = serializers.CharField(source='usr.username', read_only=True)
    operation = OperationSerializer(read_only=True)
    # street = serializers.CharField(source='usr.username', read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = ('id', 'fromdate', 'todate', 'description', 'descriptionar', 'status', 'operation',)

