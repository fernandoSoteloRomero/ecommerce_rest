from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer
from rest_framework import viewsets

#no es exactamente un modelo
#GenericViewSet no tiene incorporados los metodos list, create, destroy, update, etc
#Esto se debe a que ya vienen incorporados
class UserViewSet(viewsets.GenericViewSet):
  serializer_class = UserSerializer
  list_serializer_class = UserListSerializer
  
  def list(self, request):
    users = self.get_queryset()
    users_serializer = self.list_serializer_class(users, many = True)
    return Response(users_serializer.data, status=status.HTTP_200_OK)
  
  def get_queryset(self):
    if self.queryset is None:
      self.queryset = self.serializer_class().Meta.model.objects.filter(is_active = True).values('id', 'username', 'email', 'name')
    return self.queryset

  def create(self, request):
    user_serializer = self.serializer_class(data = request.data)
    if user_serializer.is_valid():
      user_serializer.save()
      return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'hay errores en el registro', 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    



#dos parametros
#que metodos http permitiremos que tenga esta ffuncion
#en una lista
@api_view(['GET', 'POST'])
def user_api_view(request):  
    #tod os los usuarios
    if request.method == 'GET':
      #queryset
      #el .values() te trae un diccionario de python
      users = User.objects.all().values('id','username','email','password')
      #serializar una instancia, osea 1 solo valor
      #pero esta consulta nos regresa un listado
      #por eso usamos many=True, le estamos mandando un listado de instancias
      users_serializer = UserListSerializer(users, many=True)
      return Response(users_serializer.data, status=status.HTTP_200_OK)
    # create
    elif request.method == 'POST':
      #permite hacer un proceso de validacion netamente
      #convertira el modelo a JSON
      #si yo le paso un json, el comparara el modelo convertido a JSON y validara si los datos enviados por el front 
      user_serializer = UserSerializer(data=request.data)
      #validation
      if user_serializer.is_valid():
        #la registra en la base de datos, la serealiza y la manda en .data
        user_serializer.save()
        return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
      return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk= None):
  #Consulta, queryset
  user = User.objects.filter(id = pk).first()
  
  #Validacion
  if user:
    #retrieve
    if request.method == 'GET':
      user_serializer = UserSerializer(user)
      return Response(user_serializer.data, status=status.HTTP_200_OK)
    #update
    elif request.method == 'PUT':
      #el entiende que va a ser una actualizacion con la informacion que le estas pasando
      user_serializer = UserSerializer(user, data=request.data )
      if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_200_OK)
      return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete
    elif request.method == 'DELETE':
      user.delete()
      message = f'El usuario {user.username} fue eliminado correctamente'
      return Response({'message':message}, status=status.HTTP_200_OK)

  return Response({'message': 'No se ha encontrado un usuario con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
  
  