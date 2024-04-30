from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers


class MeasureUnit(serializers.ModelSerializer):
  class Meta:
    model = MeasureUnit
    exclude = ('state')
    

class CategoryProduct(serializers.ModelSerializer):
  class Meta:
    model = CategoryProduct
    exclude = ('state')
    

class Indicator(serializers.ModelSerializer):
  class Meta:
    model = Indicator
    exclude = ('state')
