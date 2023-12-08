from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    ...