from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from Auction.models import Bids, AuctionStatus, Auction
from Operation.models import Operation

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime
from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['POST'])
def Bids_add(request):
    try:
        if request.method == 'POST':
            S = Auction.objects.filter(id=request.data['auction'])
            Status=S[0].status
            print(Status)
            #Status='OPEN'
            if str(Status) == 'OPEN':
                b = Bids.objects.filter(auction=request.data['auction']).order_by('-amount')
                print(b)
                if b.exists():
                    lastbids = b[0].amount
                    print(lastbids)
                    print(request.data['amount'])
                    if Decimal(request.data['amount']) > lastbids:
                        print('hiii')
                        Bids.objects.create(auction_id=request.data['auction'],
                                            subscriber_id=request.data['user'],
                                            amount=request.data['amount'],
                                            biddatetime=datetime.today(),
                                            created_at=datetime.today(),
                                            updated_at=datetime.today(),
                                            )
                        return JsonResponse({'message': 'Bids added successfully!'}, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse({'message': 'Bids Failed,less than last bids'}, status=status.HTTP_404_NOT_FOUND)

                else:
                    o = Auction.objects.filter(id=request.data['auction'])
                    oper = o[0].operation_id
                    startbids=Operation.objects.filter(id=oper)
                    startbid = startbids[0].price
                    print(startbid)
                    if Decimal(request.data['amount']) > startbid:
                        Bids.objects.create(auction_id=request.data['auction'],
                                            subscriber_id=request.data['user'],
                                            amount=request.data['amount'],
                                            biddatetime=datetime.today(),
                                            created_at=datetime.today(),
                                            updated_at=datetime.today(),
                                            )
                        return JsonResponse({'message': 'Bids added successfully!'}, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse({'message': 'Bids Failed,less than started bids'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse({'message': 'Auction Closed'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({'message': 'Bids Failed'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return JsonResponse({'message': 'Error'}, status=status.HTTP_404_NOT_FOUND)


class BidsViews(viewsets.ModelViewSet):
    queryset = Bids.objects.all()
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    serializer_class = BidsSerializer

