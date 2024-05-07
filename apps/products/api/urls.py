from django.urls import path
from apps.products.api.views.general_views import CategoryProductAPIView, IndicatorAPIView, MeasureunitListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveAPIView

urlpatterns = [
  path('measure_unit', MeasureunitListAPIView.as_view(), name='measure_unit'),
  path('indicator_list', IndicatorAPIView.as_view(), name='indicator_list'),
]
