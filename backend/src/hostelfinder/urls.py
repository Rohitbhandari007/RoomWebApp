from django.contrib import admin
from django.urls import path
from main.views import PostView
from users.views import RegisterView, LoginView
from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='post'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    



]
