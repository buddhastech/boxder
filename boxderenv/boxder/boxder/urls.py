
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', index, name='inicio'),
    path('', include('assets_users.urls')),
]

