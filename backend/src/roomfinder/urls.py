from django.contrib import admin
from django.urls import path, include
from core.views import PostView, PostCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='test'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
