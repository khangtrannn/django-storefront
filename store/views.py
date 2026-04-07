from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer

class ProductList(ListCreateAPIView):
  # def get_queryset(self):
  #   return Product.objects.select_related('collection').all()
  
  # def get_serializer_class(self):
  #   return ProductSerializer
  
  queryset = Product.objects.select_related('collection').all()
  serializer_class = ProductSerializer
  
  def get_serializer_context(self):
    return {'request': self.request}
  
class ProductDetail(APIView):
  def get(self, request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)
  
  def put(self, request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def delete(self, request, id):
    product = get_object_or_404(Product, pk=id)
    
    if product.order_items.count() > 0:
      return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(ListCreateAPIView):
  queryset = Collection.objects.annotate(products_count=Count('product')).all()
  serializer_class = CollectionSerializer
  
class CollectionDetail(ListCreateAPIView):
  queryset = Collection.objects.annotate(products_count=Count('product')).all()
  serializer_class = CollectionSerializer
  