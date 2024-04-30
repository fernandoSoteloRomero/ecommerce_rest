from django.urls import path
from apps.products.api.views.general_views import MeasureUnitList, IndicatorList, CategoryProductList
from apps.products.api.views.product_views import product_api_view, product_detail_api_view


urlpatterns = [
  path('measure_unit', MeasureUnitList, name='measure_unit'),
  path('indicator_list', IndicatorList, name='indicator_list'),
  path('category_product_list', CategoryProductList, name='category_product_list'),
  path('product/', product_api_view, name='product'),
  path('product/<int:pk>', product_detail_api_view, name='product_detail')
]
