from pydoc import classname
from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

# Le indicamos a Django que los campos created y updated son de solo lectura
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields= "created", "updated"

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields= "created", "updated"
