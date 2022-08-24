# basic URL config.
# from django.template.defaulttags import url
# from django.conf.urls import url
from django.urls import include, path
# importing routers
from .views import *
from . import views

# define the router

# specify URL Path for rest_framework

urlpatterns = [
    path(r'complains_list', views.Complains_list),
    path(r'complains_specific/<int:pk>', views.Complains_detail),
    path(r'complains_images', views.ImageComplainsViews),
]
