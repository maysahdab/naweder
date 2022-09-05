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
router.register(r'complains-images', ImageComplainsViews, basename='complains_images')
router.register(r'complain-get', ComplainsViews, basename='complain_get')
router.register(r'complains-all', AllComplainsViews, basename='all_complains')
router.register(r'my-complain', MyComplainsViews, basename='my_complain')
# router.register(r'my-complain2', MyComplainsViews2, basename='my_complain2')

# specify URL Path for rest_framework
urlpatterns = [
    path('complain-add', views.Complain_add),
    # path('complains-specific/<int:pk>', views.Complains_detail),
    path('complain-delete/<int:pk>', views.Complain_delete),
    path('complain-update/<int:pk>', views.Complain_update),
    path('', include(router.urls)),
]
