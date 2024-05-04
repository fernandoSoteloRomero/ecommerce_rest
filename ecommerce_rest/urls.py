from django.contrib import admin
from django.urls import path, include
from apps.users.auth import Login, Logout
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path( 'usuario/', include('apps.users.api.urls') ),
    path( 'products/', include('apps.products.api.urls') ),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]
