from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from .rol import Rol

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Crea y guarda un usuario con el nombre de usuario y contraseña proporcionados.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """
        Crea y guarda un superusuario con el nombre de usuario y contraseña proporcionados.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractUser):

    # class Genero(models.TextChoices):
    #     SELECCIONE = "Seleccione", _("Seleccione")
    #     MASCULINO = "Masculino", _("Masculino")
    #     FEMENINO = "Femenino", _("Femenino")
    #     OTRO = "Otro", _("Otro")

    rol = models.ForeignKey(Rol, related_name='Rol', on_delete=models.CASCADE)
    cedula = models.PositiveIntegerField('Cedula')
    nacimiento = models.DateField('Nacimiento')
    genero = models.CharField(
        'Genero',
        max_length=15,
        # choices=Genero,
        # default=Genero.SELECCIONE,
        )
    rh = models.CharField('Tipo de sangre', max_length = 50)
    direccion = models.CharField('Direccion', max_length = 255)
    telefono = models.PositiveIntegerField('Telefono')


    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'