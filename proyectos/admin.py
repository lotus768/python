from django.contrib import admin
from .models import TipoDocu, CateProyec, Proyecto, Documento

# Register your models here.

class TipoDocuModel(admin.ModelAdmin):
    list_display = ["nomTipoDo"]
    list_display_links = ["nomTipoDo"]
    list_filter = ["nomTipoDo"]
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)

class CateProyecModel(admin.ModelAdmin):
    list_display = ["lenguaje"]
    list_display_links = ["lenguaje"]
    list_filter = ["lenguaje"]
    class Meta:
        model = CateProyec
admin.site.register(CateProyec)

class ProyectoModel(admin.ModelAdmin):
    list_display = ["nomPro"]
    list_display_links = ["nomPro"]
    list_filter = ["nomPro"]
    class Meta:
        model =Proyecto
admin.site.register(Proyecto)

class DocumentoModel(admin.ModelAdmin):
    list_display = ["idPro"]
    list_display_links = ["idPro"]
    list_filter = ["idPro"]
    class Meta:
        model = Documento
admin.site.register(Documento)