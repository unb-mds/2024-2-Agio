from django.test import TestCase
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from apps.dashboard.models import UserTable

class UserTableModelTests(TestCase):
    def test_create_user(self):
        user = UserTable.objects.create(
            id = 1,
            name = "Test user",
            email = "test@example.com",
            password = make_password("testpassword")
        )
        self.assertEqual(user.name, "Test user")
        self.assertEqual(user.email, "test@example.com")
        self.assertNotEqual(user.password, "testpassword")
        self.assertTrue(check_password("testpassword", user.password))

    def test_password_unhashed(self):
        user = UserTable.objects.create(
            id = 1,
            name = "Test user",
            email = "test@example.com",
            password = make_password("testpassword")
        )
        user.name = "Updated user"
        user.save()
        self.assertTrue(check_password("testpassword", user.password))

    def test_invalid_email(self):
        user = UserTable.objects.create(
            id = 2,
            name = "Invalid email",
            email = "invalid-email",
            password = make_password("password")
    )
        with self.assertRaises(ValidationError):
            user.full_clean()
            user.save()