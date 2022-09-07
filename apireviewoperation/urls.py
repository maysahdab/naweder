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

router.register(r'get-my-reviews', MyOperationReviewsViews, basename='get_my_reviews')

# specify URL Path for rest_framework

urlpatterns = [
    # path('review-product-add', views.ReviewProduct_add),
    # path('review-product-delete/<int:pk>', views.ReviewProduct_delete),
    # path('review-product-update/<int:pk>', views.ReviewProduct_update),
    path('', include(router.urls)),
]
