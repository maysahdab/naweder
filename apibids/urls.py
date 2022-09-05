from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'bids-get', BidsViews, basename='Bids_,get')

# specify URL Path for rest_framework

urlpatterns = [
    path('bids-add', views.Bids_add),
    path('', include(router.urls)),
]
