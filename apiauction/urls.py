from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
# router.register(r'complains-images', ImageComplainsViews, basename='complains_images')
router.register(r'auction-all', AuctionEndTodayViews, basename='auction_all')
router.register(r'animals', AnimalViews, basename='animals')
router.register(r'bids', BidsViews, basename='bids')
router.register(r'highest-bids', HighestBidsViews, basename='highest_bids')
router.register(r'auction-animal', AuctionAnimalViews, basename='auction_animal')

# router.register(r'auction-info/<int:id>', AuctionByIdViews, basename='auction_info')
router.register(r'auction-info', AuctionByIdViews, basename='auction_info')

# specify URL Path for rest_framework
urlpatterns = [
    # path('complain-add', views.Complain_add),
    # path(r'auction-info', AuctionByIdViews.as_view()),
    # path(r'auction-info', views.AuctionByIdViews),  # /<int:pk>
    path(r'last-added-auctions', LastAddedAuctionViews.as_view()),
    path('', include(router.urls)),
]
