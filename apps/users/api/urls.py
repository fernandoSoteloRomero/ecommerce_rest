from django.urls import path
# from apps.users.api.views import UserAPIView
from apps.users.api.views import user_api_view, user_detail_api_view

urlpatterns = [
  # path( 'usuarios/', UserAPIView.as_view(), name='usuario_api' )
  path( 'usuarios/', user_api_view, name='usuario_api' ),
  path('usuario/<int:pk>/', user_detail_api_view, name = 'user_detail_api_view')
]
  