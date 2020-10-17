from django.contrib import admin
from django.urls import path, include
from main.views import PostView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', PostView.as_view(), name='test'),
]
