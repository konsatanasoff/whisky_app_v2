from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Whisky collection",
        default_version='v1',
        description="API documentation",
    ),
)

urlpatterns = [
    path('', include('common_api.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users_api.urls')),
    path('drinks/', include('drinks_api.urls')),
    path('about/', include('common_api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
