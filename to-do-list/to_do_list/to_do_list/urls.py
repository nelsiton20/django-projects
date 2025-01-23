from django.contrib import admin
from django.urls import path

from django.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', include('tasks.urls')),
    path('logout/', views.logout_view, name='logout')
]
