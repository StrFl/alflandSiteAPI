"""alflandAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from RegAPI.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_schema', get_schema_view(title='API Schema', description='po gaidu'), name='api_schema'),
    path('api/docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
    path('api/download/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),


    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),


    path('api/view/', RegAPIList.as_view()),
    
    
    path('api/bal/<int:transaction>&<str:boughtObject>/', BalanceAPIView.as_view()),

 
     
]
