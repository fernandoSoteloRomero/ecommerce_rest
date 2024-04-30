from rest_framework import serializers
from apps.users.models import User

#modelSerializer porque hara un serializador de un modelo
#convertir una instancia de un modelo en especifico en un JSON
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"
  
  #sobreescribir el metodo create del serializer
  def create(self, validated_data):
    #creas una instancia de User y le pasas toda la informacion que te mandan del front a la instancia User y esto genera un User con toda la informacion
    user = User(**validated_data)
    #le dices que en el campo password encripte la contraseña con el metodo set_password
    user.set_password(validated_data['password'])
    # lo guardas en la base de datos
    user.save()
    #retornas el usuario creado y su password encriptada
    return user
  
  def update(self, instance, validated_data):
    #aqui lo que hacemos es que actualice el usuario que le pasamos desde el front normalmente, utilizando el metodo update nativo sin sobreescribirse
    updated_user = super().update(instance, validated_data)
    #dentro de el updated_user entramos a su valor password y se la encriptamos
    updated_user.set_password(validated_data['password'])
    updated_user.save()
    return updated_user

class UserListSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
  
  #esto solo afecta al retorno de un listado, no a los otros metodos como update o create
  #como queremos que el serializador muestre la informacion
  def to_representation(self, instance):
    return {
      'id': instance['id'],
      'username': instance['username'],
      'email': instance['email'],
      'password': instance['password']
    }