from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'get-ecom-product', EcomProductGetByidViews, basename='EcomProductGet')

# specify URL Path for rest_framework
urlpatterns = [
    path('ecom-product-add', views.ReviewProduct_add),
    path('ecom-product-update/<int:pk>', views.ReviewProduct_update),
    path('ecom-product-delete/<int:pk>', views.EcomProduct_delete),
    path('', include(router.urls)),
]
