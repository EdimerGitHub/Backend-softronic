from softronicApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password','rol','first_name','last_name','cedula','nacimiento','genero','rh','email','telefono','direccion','is_active','date_joined']