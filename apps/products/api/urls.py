from django.urls import path
from apps.products.api.views.general_views import IndicatorViewSet, MeasureunitViewSet

urlpatterns = [
  path('measure_unit', MeasureunitViewSet.as_view(), name='measure_unit'),
  path('indicator_list', IndicatorViewSet.as_view(), name='indicator_list'),
]
