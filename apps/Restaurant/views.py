from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Restaurant, Category, Product, Details
)
from .serializer import (
    RestaurantSerializer, CategorySerializer, ProductSerializer, DetailsSerializer
)


class RestaurantCreateListView(APIView):
    
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        restaurant = request.data
        serializer = RestaurantSerializer(data=restaurant)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantUpdateView(APIView):
    
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        new_data = request.data
        serializer = RestaurantSerializer(restaurant, data=new_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        new_data = request.data
        serializer = RestaurantSerializer(restaurant, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryCreateListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DetailsCreateListView(generics.ListCreateAPIView):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()

class DetailsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()
