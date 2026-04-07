from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
  def get(self, request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)
  
  def post(self, request):
    # serializer = ProductSerializer(data=request.data)
    # if serializer.is_valid():
    #   serializer.validated_data
    #   return Response('ok')
    # else:
    #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


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

@api_view()
def collection_detail(request, pk):
  return Response('ok')