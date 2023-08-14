from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user@test.com',
            password='test'
        )
        self.assertEqual(
            user.email,
            'user@test.com'
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_admin)

    def test_create_user_no_arguments(self):
        User = get_user_model()
        with self.assertRaises(TypeError):
            User.objects.create_user()

