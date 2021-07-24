# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from product.serializers import ProductSerializer
from product.models import Product

# Create your views here.
'''class ProductListApi(APIView):
    """
List all products, or create a new chambre.
"""
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)


    def get(self, request, format=None):
        products = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(commit=False)
            serializer.user=request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''
class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]
    filter_backends =[DjangoFilterBackend]
    filterset_fields=['account']
    filterset_fields=['category']







''' def get_queryset(self):
        return Product.objects.order_by('pprice')

class ProductList(ListAPIView):
       # queryset= Product.objects.filter(passby='yash')
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[SearchFilter]
    search_fields=['name']
    #search_fields=['name','price']
    #search_fields=['^name']
    #search_fields=['=name'] '''

class ProductList(ListAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields=['account']

class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the todo to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer