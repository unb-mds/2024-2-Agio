from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ProductTable
from .serializers import ProductSerializer

import csv
from io import StringIO

# Create your views here.


def dashboard_view(request):
    products = ProductTable.objects.all()
    return render(request, "dashboard/dashboard.html",
                  {"products": products})

@api_view(['GET'])
def export_dashboard_csv(request):
    """Gera um CSV e retorna como string"""
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Nome', 'Descrição', 'Preço'])  # Cabeçalhos do CSV

    for product in ProductTable.objects.all():
        writer.writerow([product.id, product.product_name, product.description, product.price])

    return Response({"csv_data": output.getvalue()}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def product_manager(request):

    if request.method == 'GET':
        product_name = request.GET.get('product')

        if not product_name:
            return Response({'error': 'Product name not provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except ProductTable.DoesNotExist:
            return Response({'error': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        product_name = request.data.get('product_name')

        if not product_name:
            return Response({'error': 'Product name not provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
        except ProductTable.DoesNotExist:
            return Response({'error': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product,
                                       data=request.data,
                                       partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product_name = request.data.get('product_name')

        if not product_name:
            return Response({'error': 'Product name not provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
            product.delete()
            return Response({'message': 'Product deleted successfully'},
                            status=status.HTTP_202_ACCEPTED)
        except ProductTable.DoesNotExist:
            return Response({'error': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)
