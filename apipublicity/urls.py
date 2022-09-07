from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'get-publicity', PublicityViews, basename='get_publicity')
# router.register(r'get-publicity-images', PublicityimagesViews, basename='get_publicity_images')
# router.register(r'post-publicity', PostPublicityViews, basename='post_publicity')

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('publicity-add', views.Publicity_add),
    path('publicity-delete/<int:pk>', views.Publicity_delete),
    path('publicity-update/<int:pk>', views.Publicity_update),
]
