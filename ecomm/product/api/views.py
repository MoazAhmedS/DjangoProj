from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import product
from .serializers import ProductSeriliz
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

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


class ProductDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = product.get_products()
    serializer_class = ProductSeriliz
    lookup_field = 'id'
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Product updated', 'data': response.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response({'message': 'Product soft-deleted'}, status=status.HTTP_200_OK)

class ProductViewSet(ModelViewSet):
    queryset = product.get_products()
    serializer_class = ProductSeriliz
    lookup_field = 'id' 
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'msg': 'Product updated', 'data': response.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response({'msg': 'Product soft-deleted'}, status=status.HTTP_200_OK)