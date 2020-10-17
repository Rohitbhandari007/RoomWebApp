from django.contrib import admin
from django.urls import path, include
from main.views import test_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', test_view, name='test')
]
