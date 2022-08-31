from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
# router.register(r'complains-images', ImageComplainsViews, basename='complains_images')
router.register(r'auction-all', AuctionViews, basename='auction_all')

# specify URL Path for rest_framework
urlpatterns = [
    # path('complain-add', views.Complain_add),
    path('', include(router.urls)),
]
