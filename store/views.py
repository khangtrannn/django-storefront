from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
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
  
class ProductDetail(RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'id'
  
  def delete(self, request, id):
    product = get_object_or_404(Product, pk=id)
    
    if product.order_items.count() > 0:
      return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(ListCreateAPIView):
  queryset = Collection.objects.annotate(products_count=Count('product')).all()
  serializer_class = CollectionSerializer
  
class CollectionDetail(RetrieveUpdateDestroyAPIView):
  queryset = Collection.objects.annotate(products_count=Count('product')).all()
  serializer_class = CollectionSerializer
  
  def delete(self, request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    
    if collection.product_set.count() > 0:
      return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    collection.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  