from django.db import models
from django.conf import settings
#from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
#modelo roles
class Roles (models.Model):
    roleNama = models.CharField(max_length=50, verbose_name="Nombre Rol")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"

     #funcion de seleccion
    def __str__(self):
        return self.roleNama

#modelo datos usuarios
class DatosUser (models.Model):
    userDNI = models.CharField(max_length=20, verbose_name="Identificacion")
    nomUser = models.CharField(max_length = 250, null=True, verbose_name = "Nomres")
    apeUser = models.CharField(max_length = 250, null=True, verbose_name = "Apellidos")
    fotoUser = models.ImageField(default='user.png', verbose_name= "Foto de perfil", upload_to="perfiles")
    teleUser = models.CharField(max_length=20, verbose_name="Numero de telefono")
    geneUser = models.CharField(max_length= 20, choices = Generos, default = "Otro", verbose_name = "Genero")
    adddata = models.DateTimeField(auto_now_add = True, null=True, verbose_name="Cargado el")
    modifiat = models.DateTimeField(auto_now= True, null=True, verbose_name="Modificado el")

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Informacion"

    #funcion de seleccion
    def __str__(self):
        return self.nomUser

#modelo detallerol
class DetaRol(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateField(auto_now_add = True, auto_now = False)
    udtuser = models.DateField(auto_now = True)
    estaRol = models.CharField(max_length = 10)

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"

    #funcion de seleccion
    def __unicode__(self):
        return self.idUser

#modelo habilidades
class HabilUser (models.Model):
    nomHabil = models.CharField(max_length=155)
    descHabil = models.TextField(max_length = 2000, verbose_name = "Descripcion de la Habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

#funcion de seleccion
    def __str__(self):
        return self.nomHabil

#modelo retes
class Rates (models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    pcrHabil = models.DecimalField(max_digits = 2,decimal_places = 1)
    udtHabil = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = "Nivel de Habilidades"
        verbose_name_plural = "Niveles de Usuario"

    #funcion de seleccion
    def __unicode__(self):
        return self.idUser
