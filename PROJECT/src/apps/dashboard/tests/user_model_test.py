from django.test import TestCase
from django.contrib.auth.hashers import check_password
from apps.dashboard.models import UserTable

class UserTableModelTests(TestCase):
    def test_create_user(self):
        user = UserTable.objects.create(
            id = 1,
            name = "Test user",
            email = "test@example.com",
            password = "testpassword"
        )
        self.assertEqual(user.name, "Test user")
        self.assertEqual(user.email, "test@example.com")
        self.assertNotEqual(user.password, "testpassword")
        self.assertTrue(check_password("testpassword", user.password))

    def test_passord_unhashed(self):
        user = UserTable.objects.create(
            id = 1,
            name = "Test user",
            email = "test@example.com",
            password = "testpassword"
        )
        user.name = "Updated user"
        user.save()
        self.assertTrue(check_password("testpassword", user.password))

    def test_invalid_email(self):
        with self.assertRaises(Exception):
            UserTable.objects.create(
                id = 2,
                name = "Invalid email",
                email = "invalid-email",
                password = "password"
        )