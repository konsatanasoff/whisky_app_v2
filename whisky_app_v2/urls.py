from django.contrib import admin
from django.urls import path, include

import users_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_api.urls'))
]
