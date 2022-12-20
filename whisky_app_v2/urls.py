from django.contrib import admin
from django.urls import path, include

import users_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users_api.urls')),
    path('drinks/', include('drinks_api.urls')),
    path('about/', include('common_api.urls')),
    path('', include('common_api.urls')),
]
