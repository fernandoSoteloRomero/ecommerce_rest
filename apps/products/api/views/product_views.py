from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


@extend_schema(
  request=ProductSerializer,
  responses={200: ProductSerializer(Product, many = True)}, 
)
@api_view(['GET', 'POST'])
def product_api_view(request):
  if request.method == 'GET':
    products = Product.objects.filter(state = True)
    products_serializer = ProductSerializer(products, many = True)
    return Response(products_serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    product_serializer = ProductSerializer(data = request.data)
    if product_serializer.is_valid():
      product_serializer.save()
      return Response({'message':'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  else:
    return Response({'message':'metodo no soportado'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk= None):
  #Consulta, queryset
  product = Product.objects.filter(id = pk).filter(state = True).first()
  
  if product:
    if request.method == 'GET':
      product_serializer = ProductSerializer(product)
      return Response(product_serializer.data, status=status.HTTP_200_OK)

    
    elif request.method == 'PUT':
      product_serializer = ProductSerializer(product,data=request.data )
      if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
      return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      product.state = False
      product.save()
      return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
  return Response({'message':'No se ha encontrado un producto con esos datos'}, status=status.HTTP_400_BAD_REQUEST)