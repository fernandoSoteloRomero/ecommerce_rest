from rest_framework import generics
from rest_framework.decorators import api_view
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import *
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(
  responses={200: MeasureUnitSerializer(MeasureUnit, many = True)}, 
)

@api_view(['GET'])
def MeasureUnitList(request):
  if request.method == 'GET':
    measureList = MeasureUnit.objects.filter(state = True)
    measureList_serializer = MeasureUnitSerializer(measureList, many=True)
    return Response(measureList_serializer.data, status=status.HTTP_200_OK)
  else:
    return Response({'message':'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@extend_schema(
  responses={200: CategoryProductSerializer(CategoryProduct, many = True)}, 
)

@api_view(['GET'])
def CategoryProductList(request):
  if request.method == 'GET':
    categoryProduct = CategoryProduct.objects.filter(state = True)
    categoryProduct_serializer = CategoryProductSerializer(categoryProduct, many = True)
    return Response(categoryProduct_serializer.data, status=status.HTTP_200_OK)
  else:
    return Response({'message':'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@extend_schema(
  responses={200: IndicatorSerializer(Indicator, many = True)}, 
)

@api_view(['GET'])
def IndicatorList(request):
  if request.method == 'GET':
    indicator = Indicator.objects.filter(state = True)
    indicator_serializer = IndicatorSerializer(indicator, many = True)
    return Response(indicator_serializer.data, status=status.HTTP_200_OK)
  else:
    return Response({'message':'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)













