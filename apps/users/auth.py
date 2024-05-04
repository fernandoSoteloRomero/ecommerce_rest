from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView
#hereda de api view
class Login(ObtainAuthToken):
  #nos llegara el usuario y la contraseña
  def post(self, request, *args, **kwargs):
    login_serializer = ObtainAuthToken.serializer_class(data=request.data, context= {'request':request})
    if login_serializer.is_valid():
      #si tiene un usuario y una contrasena en la base de datos
      user = login_serializer.validated_data['user']
      if user.is_active:
        token,created = Token.objects.get_or_create(user = user)
        user_serializer = UserTokenSerializer(user)
        if created:
          return Response({
            
            'token':token.key,
            'user': user_serializer.data,
            'message': 'Inicio de sesion exitoso'
            
          }, status=status.HTTP_201_CREATED)
        else:
          all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
          if all_sessions.exists():
            for session in all_sessions:
              session_data = session.get_decoded()
              if user.id == int(session_data.get('_auth_user_id')):
                session.delete()
          token.delete()
          token = Token.objects.create(user = user)
          return Response({
            
            'token':token.key,
            'user': user_serializer.data,
            'message': 'Inicio de sesion exitoso'
            
          }, status=status.HTTP_201_CREATED)
      else:
        return Response({'error':'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error':'Nombre de usuario o contrasena incorrectos'}, status=status.HTTP_400_BAD_REQUEST)



class Logout(APIView):
    def post(self, request, *args, **kwargs):
      print(request.data)
      token = request.data.get('token')  # Cambio request.GET por request.data para obtener datos del cuerpo del POST
      try:
        token = Token.objects.get(key=token)
      except Token.DoesNotExist:
        return Response({'error': 'El token proporcionado no es válido'}, status=status.HTTP_404_NOT_FOUND)
      
      user = token.user
      all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
      if all_sessions.exists():
        for session in all_sessions:
          session_data = session.get_decoded()
          if user.id == int(session_data.get('_auth_user_id')):
            session.delete()
  
        token.delete()
        session_message = 'Sesiones de usuario eliminadas'
        token_message = 'Token eliminado'
        return Response({
          'token_message': token_message, 
          'session_message': session_message
        }, status=status.HTTP_200_OK)
      
      return Response({'error': 'No se ha encontrado un usuario con estas credenciales'}, status=status.HTTP_400_BAD_REQUEST)














