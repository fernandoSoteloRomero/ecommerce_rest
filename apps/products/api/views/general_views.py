from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureunitListAPIView(GeneralListApiView):
  serializer_class = MeasureUnitSerializer
  
  
class IndicatorAPIView(GeneralListApiView):
  serializer_class = IndicatorSerializer
  
  
class CategoryProductAPIView(GeneralListApiView):
  serializer_class = CategoryProductSerializer