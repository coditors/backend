
from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  
    path('', include('django.contrib.auth.urls')),
    path('register/' , views.register , name="register"),
    path('v1/token/' , jwt_views.TokenObtainPairView.as_view() , name="token_obtain_pair"),
    path("v1/refresh/" ,jwt_views.TokenRefreshView.as_view() , name="token_refresh"),
    path('v1/register/',  include('rest_auth.registration.urls')),

]
