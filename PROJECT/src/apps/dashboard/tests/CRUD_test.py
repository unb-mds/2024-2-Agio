from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.dashboard.models import ProductTable
from decimal import Decimal

class ProductManagerTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'product_name': 'Test product', 
            'amount': 10, 
            'category': 'Electronics', 
            'description': 'A test product', 
            'price': 9.11
        }
        self.product = ProductTable.objects.create(**self.product_data)

    def test_GET_product_success(self):
        product = ProductTable.objects.create(
            product_name = "Test Product",
            amount = 10,
            category = "Test Category",
            description = "Test Description",
            price = Decimal('4.20')
        )
        response = self.client.get('/product-manager/', {'product': product.product_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_name'], product.product_name)
        self.assertEqual(response.data['amount'], product.amount)
        self.assertEqual(response.data['category'], product.category)
        self.assertEqual(response.data['description'], product.description)
        self.assertEqual(Decimal(response.data['price']), product.price)
        
    def test_GET_product_failure_not_found(self):
        response = self.client.get('/product-manager/', {'product': 'Non existent product'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Product not found')

    def test_GET_product_failure_no_name(self):
        response = self.client.get('/product-manager/', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Product name not provided')

    def test_POST_product_success(self):
        new_product_data = {
            'product_name': 'New product',
            'amount': 5,
            'category': 'Books',
            'description': 'A new test product',
            'price': 4.20
        }
        response = self.client.post('/product-manager/', new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['product_name'], new_product_data['product_name'])
        self.assertTrue(ProductTable.objects.filter(product_name='New product').exists())

    def test_POST_product_failure_invalid_data(self):
        invalid_data = {'price': 4.20}
        response = self.client.post('/product-manager/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_POST_failure_duplicate(self):
        response = self.client.post('/product-manager/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_PUT_product_success(self):
        update_data = {
            'product_name': self.product.product_name,
            'amount': 15,
            'category': 'Updated Category',
            'description': 'Updated description',
            'price': 6.90
        }
        response = self.client.put('/product-manager/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.product.refresh_from_db()
        self.assertEqual(self.product.amount, 15)
        self.assertEqual(self.product.category, 'Updated Category')
        self.assertEqual(self.product.description, 'Updated description')
        self.assertEqual(self.product.price, Decimal('6.90'))

    def test_PUT_product_failure_not_found(self):
        update_data = {
            'product_name': 'Non existent product',
            'amount': 5,
            'category': 'Non existent',
            'description': 'Non existent description',
            'price': 6.90
        }
        response = self.client.put('/product-manager/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_PUT_product_failure_no_name(self):
        update_data = {'price': 6.90}
        response = self.client.put('/product-manager/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_DELETE_product_success(self):
        product = ProductTable.objects.create(
            product_name = "Test Product",
            amount = 10,
            category = "Test Category",
            description = "Test Description",
            price = 4.20
        )
        response = self.client.delete('/api/products/', data = {'product_name': product.product_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(ProductTable.objects.filter(product_name=product.product_name).exists())

    def test_DELETE_product_failure_not_found(self):
        response = self.client.delete('/api/products/', data = {'product_name': 'Nonexistent Product'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_DELETE_product_failure_no_name(self):
        response = self.client.delete('/api/products/', data = {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('<title>Not Found</title>', response.content.decode())
