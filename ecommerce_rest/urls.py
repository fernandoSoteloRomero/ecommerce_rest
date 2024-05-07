from django.contrib import admin
from django.urls import path, include
from apps.users.auth import Login, Logout
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path( 'usuario/', include('apps.users.api.urls') ),
    path( 'products/', include('apps.products.api.routers') ),

    
]
