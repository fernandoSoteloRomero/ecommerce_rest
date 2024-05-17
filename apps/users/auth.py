from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session
from rest_framework.views import APIView
from apps.users.authentication_mixins import Authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomSerializer
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class Login(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  
  def post(self, request, *args, **kwargs):
    username = request.data.get('username', '')
    password = request.data.get('password', '')
    user = authenticate(
      username = username,
      password = password
    )
    
    if user:
      login_serializer = self.serializer_class(data = request.data)
      if login_serializer.is_valid():
        user_serializer = CustomSerializer(user)
        return Response({
          'token': login_serializer.validated_data.get('access'),
          'refresh_token': login_serializer.validated_data.get('refresh'),
          'user': user_serializer.data,
          'message':'Inicio de sesión exitoso'
        }, status=status.HTTP_200_OK
                        )
        
      return Response({'message':'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message':'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)



class Logout(GenericAPIView):
  def post(self, request, *args, **kwargs):
    user = User.objects.filter(id = request.data.get('user', 0))
    if user.exists():
      RefreshToken.for_user(user.first()) 
      return Response({'message':'Sesión  cerrada correctamente'}, status=status.HTTP_200_OK)
    return Response({'message':'Usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)





