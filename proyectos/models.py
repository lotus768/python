from django.db import models
from django.conf import settings
from userdata.models import DatosUser
#from ckeditor.fields import RichTextField


# Create your models here.

#modelo tipo documento
class TipoDocu (models.Model):
    nomTipoDo = models.CharField(max_length=45, verbose_name="Tipo documento")

    class Meta:
        verbose_name = "Tipos de documento"
        verbose_name_plural = "Tipo de documento"

     #funcion de seleccion
    def _str_(self):
        return self.nomTipoDo

#modelo categoria proyecto
class CateProyec (models.Model):
    lenguaje = models.CharField(max_length=250,verbose_name="Lenguaje")
    motorBd = models.CharField(max_length=100, verbose_name="Motor BD")
    arqui = models.CharField(max_length=250,verbose_name="arquitectura")

    class Meta:
        verbose_name = "Categoria Del Proyecto"
        verbose_name_plural = "Categoria de Proyectos"
    def _str_(self):
        return self.lenguaje

#modelo proyecto
class Proyecto (models.Model):
    idCate = models.ForeignKey(CateProyec, on_delete = models.CASCADE, verbose_name = "Identificador del Proyecto")
    nomPro = models.CharField(max_length=250,verbose_name="Nombre de Proyecto")
    desProyec = models.CharField(max_length=250,verbose_name="Descripción")
    imgPro = models.ImageField(default='proyec.png', verbose_name= "Imagen de Proyecto", upload_to="proyecto/img")
    fechaIni = models.DateTimeField(auto_now_add=False, verbose_name="Fecha Inicio")
    fechaFi = models.DateTimeField(auto_now_add=False, verbose_name="Fecha Final")
    url = models.CharField(max_length=250,verbose_name="URL")
    estaPro = models.CharField(max_length=100, verbose_name="Estado")

    class Meta:
        verbose_name = "Datos del Proyecto"
        verbose_name_plural = "Proyectos"
    def _unicode_(self):
        return self.nomPro

#modelo documento
class Documento (models.Model):
    idTiDo = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name = "Tipo Documento")
    idPro = models.ForeignKey(Proyecto, on_delete = models.CASCADE, verbose_name = "Proyecto")
    iduser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Usuario")
    nomdocu = models.CharField(max_length=250, verbose_name="Nombre Documento")
    patDocu = models.CharField(max_length=200,verbose_name="URL git")

    class Meta:
        verbose_name = "Documento "
        verbose_name_plural = "Documentos "
    def _unicode_(self):
        return self.idPro



