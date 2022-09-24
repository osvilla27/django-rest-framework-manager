from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from store.api.router import router_store
from customer.api.router import router_customer

schema_view = get_schema_view(
    openapi.Info(
        title="Manager - API",
        default_version='v1',
        description="API DOC de Manager",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="oscaravg27@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('manager/', admin.site.urls),
    path('api/', include('accounts.api.router')),
    path('api/', include('store.api.router')),
    path('api/', include(router_store.urls)),
    path('api/', include(router_customer.urls)),
    
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
