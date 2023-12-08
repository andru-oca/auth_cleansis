from django.db import models
from django.db.models import Model

# Create your models here.

class Producto(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    nombre  =  models.CharField(max_length=100, default="Nombre x")
    categoria  =  models.CharField(max_length=100, default="Categoria x", blank=False, null=False)
    codigo  =  models.IntegerField (blank=False,null=False)
    precio  =  models.IntegerField (blank=False,null=False)


    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

class Meta:
    db_table = "Product_table"


    def __str__(self):
        return f"El producto es: {self.nombre}, categoria:{self.categoria}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
