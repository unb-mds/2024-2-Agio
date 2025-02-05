from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from dashboard.models import ProductTable

# Create your tests here.

class ProductManagerTests(TestCase):

    def setUp(self):
        self.client = APIClient
        self.product_data = {
            'product_name': 'Test product', 
            'amount': 10, 
            'category': 'Electronics', 
            'description': 'A test product', 
            'price': 9.11
        }
        self.product = ProductTable.objects.create(**self.product_data)

    def test_GET_product_success(self):
        response = self.client.get('/products/', {'product': self.product.product_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_name'], self.product.product_name)
        self.assertEqual(response.data['amount'], self.product.amount)
        self.assertEqual(response.data['category'], self.product.category)
        self.assertEqual(response.data['description'], self.product.description)
        self.assertEqual(response.data['price'], self.product.price)
        
    def test_GET_product_failure_not_found(self):
        response = self.client.get('/products/', {'product': 'Non existent product'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Product not found')

    def test_GET_product_failure_no_name(self):
        response = self.client.get('/products/')
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
        response = self.client.post('/products/', new_product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['product_name'], new_product_data['product_name'])
        self.assertTrue(ProductTable.objects.filter(product_name = 'New product').exists())

    def test_POST_product_failure_invalid_data(self):
        invalid_data = {'price': 4.20}
        response = self.client.post('/products/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_POST_failure_duplicate(self):
        response = self.client.post('/products/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_PUT_product_success(self):
        update_data = {
            'product_name': self.product.product_name,
            'amount': 15,
            'category': 'Updated Category',
            'description': 'Updated description',
            'price': 6.90
        }
        response = self.client.put('/products/', update_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.product.refresh_from_db()
        self.assertEqual(self.product.amount, 15)
        self.assertEqual(self.product.category, 'Updated Category')
        self.assertEqual(self.product.description, 'Updated description')
        self.assertEqual(self.product.price, 6.90)

    def test_PUT_product_failure_not_found(self):
        update_data = {
            'product_name': 'Non existent product',
            'amount': 5,
            'category': 'Non existent',
            'description': 'Non existent description',
            'price': 6.90
        }
        response = self.client.put('/products/', update_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_PUT_product_failure_no_name(self):
        update_data = {'price': 6.90}
        response = self.client.put('/products/', update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_PUT_product_partial_success(self):
        update_data = {'product_name': self.product.product_name, 'price': 6.90}
        response = self.client.put('/products/', update_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 6.90)

    def test_DELETE_product_success(self):
        response = self.client.delete('/products/', {'product': self.product.product_name})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertFalse(ProductTable.objects.filter(product_name=self.product.product_name).exists())

    def test_DELETE_product_failure_not_found(self):
        response = self.client.delete('/products/', {'product': 'Non existent product'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Product not found')

    def test_DELETE_product_failure_no_name(self):
        response = self.client.delete('/products/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Product name not provided')