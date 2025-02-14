from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.dashboard.models import ProductTable

class DashboardViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product1 = ProductTable.objects.create(
            product_name="Product 1", 
            description="Description 1", 
            price=10.00
        )
        self.product2 = ProductTable.objects.create(
            product_name="Product 2", 
            description="Description 2", 
            price=20.00
        )

    def test_dashboard_view_status(self):
        response = self.client.get(reverse('dashboard/view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard_view_template(self):
        response = self.client.get(reverse('dashboard/view'))
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_dashboard_view_context(self):
        response = self.client.get(reverse('dashboard/view'))
        products = response.context['products']
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].product_name, "Product 1")
        self.assertEqual(products[1].product_name, "Product 2")

    def test_dashboard_view_no_products(self):
        ProductTable.objects.all().delete()
        response = self.client.get(reverse('dashboard/view'))
        products = response.context['products']
        self.assertEqual(len(products), 0)