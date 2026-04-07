from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view()
def product_list(request):
  return Response('ok')

@api_view()
def product_detail(request, id):
  return Response('ok')