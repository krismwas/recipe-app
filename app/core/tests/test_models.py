from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "chrismwangi@gmail.com"
        password = "password1234"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_user_normalized(self):
        """Test that the new email for user is normalized"""
        email = "chris@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email, password="password1234"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None
            )

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com", "pass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
