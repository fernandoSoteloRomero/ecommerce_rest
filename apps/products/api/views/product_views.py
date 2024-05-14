from rest_framework import status, viewsets
from apps.products.api.serializers.product_serializers import ProductSerializer
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = ProductSerializer.Meta.model.objects.filter(state = True)
  
  def create(self, request):
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
  def update(self, request, pk = None):
    product = self.queryset.filter(id = pk).first()
    if product:
      product_serializer = self.serializer_class(product, data=request.data)
      if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
      return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'Error':'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

  
  def destroy(self, request, pk = None):
    product = self.get_queryset().filter(id = pk).first()
    if product:
      product.state = False
      product.save()
      return Response({'message':'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'Error':'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
  