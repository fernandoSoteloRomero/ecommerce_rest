from apps.products.models import Product
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import CategoryProductSerializer, MeasureUnitSerializer

class ProductSerializer(serializers.ModelSerializer):
  # measure_unit = MeasureUnitSerializer()
  # category_product = CategoryProductSerializer()
  class Meta:
    model = Product
    exclude = ('state','created_date', 'modified_date', 'deleted_date')
  
  
  def to_representation(self, instance):
    return {
      'name': instance.name,
      'id': instance.id,
      'description': instance.description,
      'image': instance.image or '',
      'measure_unit': instance.measure_unit.description,
      'category_product': instance.category_product.description,
    }
    
