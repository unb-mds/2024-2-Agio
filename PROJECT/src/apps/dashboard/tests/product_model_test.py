from django.test import TestCase
from apps.dashboard.models import ProductTable

class ProductTableModelTests(TestCase):
    def test_create_product(self):
        product = ProductTable.objects.create(
            product_name="Test Product",
            amount=10,
            category="Test Category",
            description="Test Description",
            price=10.00
        )
        self.assertEqual(product.product_name, "Test product")
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.category, "Test category")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 10.00)
    
    def test_default_values(self):
        product = ProductTable.objects.create(
            product_name="Default test",
            amount=10,
            price=10.00
        )
        self.assertEqual(product.category, "Sem categoria")
        self.assertEqual(product.description, "Sem descrição")

    def test_unique_constraint(self):
        product = ProductTable.objects.create(
            product_name="Unique product",
            amount=1,
            price=10.00
        )
        with self.assertRaises(Exception):
            ProductTable.objects.create(
                product_name="Default test",
                amount=10,
                price=10.00
            )

    def test_string_representation(self):
        product = ProductTable(product_name = "String representation test")
        self.assertEqual(str(product), "String representation test")