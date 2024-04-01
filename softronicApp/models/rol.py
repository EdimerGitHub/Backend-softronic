from django.db import models
#from .user import User

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=255)
    
