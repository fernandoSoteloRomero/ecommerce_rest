from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# algunos de los modelos que se van a utilizar dentro de productos


class MeasureUnit(BaseModel):

  description = models.CharField( 'Descripcion',max_length=50, blank=False, null = False, unique=True)
  historical = HistoricalRecords()
  
  @property
  def _history_user(self):
    return self.changed_by
  
  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  
  
  
  
  def __str__(self):
    return f'{self.id} {self.description}'

  class Meta:
    verbose_name = 'Unidad de medida'
    verbose_name_plural = 'Unidades de medidas'

class CategoryProduct(BaseModel):
  description = models.CharField(max_length=50, unique=True, null=False, blank=False)
  historical = HistoricalRecords()
  
  @property
  def _history_user(self):
    return self.changed_by
  
  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  
  def __str__(self):
    return f'{self.id} {self.description}'

  class Meta:
    verbose_name = 'Categoria de producto'
    verbose_name_plural = 'Categoria de productos'


class Indicator(BaseModel):

  descount_value = models.PositiveIntegerField(default=0)
  category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
  
  
  historical = HistoricalRecords()
  
  @property
  def _history_user(self):
    return self.changed_by
  
  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  
  def __str__(self):
    return f'Oferta de la categoria {self.category_product} : ${self.descount_value}%'

  class Meta:
    verbose_name = 'Indicador de oferta'
    verbose_name_plural = 'Indicadores de ofertas'


class Product(BaseModel):
  name = models.CharField('nombre de producto', max_length=150, unique=True, blank=False, null=False)
  description = models.TextField('Descripcion de producto', blank=False, null=False)
  image = models.ImageField('imagen del producto', upload_to='products/', null=True, blank=True)
  historical = HistoricalRecords()
  measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
  category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
  @property
  def _history_user(self):
    return self.changed_by
  
  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'