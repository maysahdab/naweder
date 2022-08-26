# basic URL config.
# from django.template.defaulttags import url
# from django.conf.urls import url
from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'complains_images', ImageComplainsViews, basename='complains_images')
router.register(r'complains', ComplainsViews, basename='complains')
router.register(r'all_complains', AllComplainsViews, basename='all_complains')

# specify URL Path for rest_framework

urlpatterns = [
    path(r'complains_list', views.Complains_list),
    path(r'complains_specific/<int:pk>', views.Complains_detail),
    path('api/', include(router.urls)),
]
