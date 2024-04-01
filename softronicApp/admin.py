from django.contrib import admin
from .models.rol import Rol
from .models.user import User

# Registro los modelos



admin.site.register(User)
admin.site.register(Rol)