from Auction.models import Bids, AuctionStatus, Auction
from rest_framework import serializers


class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids
        fields = ('id','auction_id', 'biddatetime', 'amount', 'subscriber_id', 'win')
        # fields = '__all__'
        depth = 1
