from django.contrib import admin

# Register your models here.
from sistema_awa.models import variables,awa


class adminAwa(admin.ModelAdmin):
    list_display=("Fecha_y_hora","Temperatura","Humedad","OD")
    date_hierarchy="Fecha_y_hora"

admin.site.register(awa,adminAwa)