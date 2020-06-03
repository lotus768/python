from django.contrib import admin

# Register your models here.
from .models import Roles, DatosUser, DetaRol, HabilUser, Rates

#modelo roles 
class RolesModel(admin.ModelAdmin):
    list_display = ["roleNama"]
    list_display_links = ["roleNama"]
    list_filter = ["roleNama"]
    class Meta:
        model = Roles
admin.site.register(Roles)

#modelo datos del usuario 
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nomUser"]
    list_display_links = ["nomUser"]
    list_filter = ["nomUser"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)

#modelo deta del rol 
class DetaRolModelo (admin.ModelAdmin):
    list_display = ["idUser"]
    list_display_links = ["idUser"]
    list_filter = ["idUser"]
    class Meta:
        model = DetaRol
admin.site.register(DetaRol)

# model Habil usuario
class HabilUserModel(admin.ModelAdmin):
    list_display = ["nomHabil"]
    list_display_links = ["nomHabil"]
    list_filter = ["nomHabil"]
    class Meta:
        model = HabilUser
admin.site.register(HabilUser)

#modelo rates 
class RatesModelo (admin.ModelAdmin):
    list_display = ["idUser"]
    list_display_links = ["idUser"]
    list_filter = ["idUser"]
    class Meta:
        model = Rates
admin.site.register(Rates)
