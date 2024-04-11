from softronicApp.models.rol import Rol
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','nombre']