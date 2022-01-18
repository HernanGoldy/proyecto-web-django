from django.contrib import admin
from .models import Servicio

# Register your models here.

# Para que aparezcan los campos created y udated en el admin de Django
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
