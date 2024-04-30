from django.db import models

# Create your models here.
class BaseModel(models.Model):

  id = models.AutoField(primary_key=True)
  state = models.BooleanField('Estado', default=True)
  created_date = models.DateField('fecha de creacion',auto_now=False, auto_now_add=True)
  modified_date = models.DateField('fecha de modificacion',auto_now=True, auto_now_add=False)
  deleted_date = models.DateField('fecha de eliminacion',auto_now=True, auto_now_add=False)

  class Meta:
    # esta prop significa que no se creara en la base de datos como tabla, servira para la creacion de otros modelos
    abstract = True
    verbose_name = ("Modelo base")
    verbose_name_plural = ("Modelos base")

