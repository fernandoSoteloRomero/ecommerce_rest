from django.urls import path
from apps.products.api.views.general_views import MeasureUnitList, IndicatorList, CategoryProductList


urlpatterns = [
  path('measure_unit', MeasureUnitList, name='measure_unit'),
  path('indicator_list', IndicatorList, name='indicator_list'),
  path('category_product_list', CategoryProductList, name='category_product_list'),
]
  