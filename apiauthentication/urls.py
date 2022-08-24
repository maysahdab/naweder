from django.urls import path, include
from .views import RegisterUserAPIView, ChangePasswordView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register', RegisterUserAPIView.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='get_token'),
    # path('logout', LogoutAPIView.as_view(), name='logout'),
    path('changePassword', ChangePasswordView.as_view(), name='change_password'),
    path('profile', ProfileView.as_view(), name='profile'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('refreshToken', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifyToken', TokenVerifyView.as_view(), name='verify_token'),
]
