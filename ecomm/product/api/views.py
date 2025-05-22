from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import product
from .serializers import ProductSeriliz
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = product.get_products()
        serializer = ProductSeriliz(products, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSeriliz(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductUpdateView(APIView):
    def put(self, request, id):
        prod = get_object_or_404(product, id=id)
        serializer = ProductSeriliz(instance=prod, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
