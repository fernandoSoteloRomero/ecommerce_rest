from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.models import MeasureUnit, Indicator, CategoryProduct


class MeasureunitViewSet(viewsets.GenericViewSet):
  

  model = MeasureUnit
  serializer_class = MeasureUnitSerializer
  queryset = MeasureUnitSerializer.Meta.model.objects.filter(state=True)

  def list(self, request):
    """
      
    """
    # Obtener todas las unidades de medida del queryset
    measure_units_list = self.queryset

    # Serializar las unidades de medida
    serializer = self.serializer_class(measure_units_list, many=True)

    # Devolver la respuesta serializada
    return Response(serializer.data)
    
  
  
class IndicatorViewSet(viewsets.ViewSet):
  model = Indicator
  serializer_class = IndicatorSerializer
  queryset = IndicatorSerializer.Meta.model.objects.filter(state=True)

  def list(self, request):
    """
      
    """
    # Obtener todas las unidades de medida del queryset
    indicators_list = self.queryset

    # Serializar las unidades de medida
    serializer = self.serializer_class(indicators_list, many=True)

    # Devolver la respuesta serializada
    return Response(serializer.data)  
  
  
class CategoryProductViewSet(viewsets.ViewSet):
  model = CategoryProduct
  serializer_class = CategoryProductSerializer
  queryset = CategoryProductSerializer.Meta.model.objects.filter(state=True)
  
  def list(self, request):
  # Obtener todas las unidades de medida del queryset
    category_products = self.queryset

  # Serializar las unidades de medida
    serializer = self.serializer_class(category_products, many=True)

  # Devolver la respuesta serializada
    return Response(serializer.data)  
  