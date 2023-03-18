from django.test import TestCase
from .models import CustomUser, Profile, PotentialProduct
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm

class CustomUserModelTestCase(TestCase):
    def test_create_custom_user(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_create_profile(self):
        profile = Profile.objects.create(
            staff=self.user,
            phone='1234567890',
            address='123 Test Street'
        )
        self.assertEqual(profile.staff, self.user)
        self.assertEqual(profile.phone, '1234567890')
        self.assertEqual(profile.address, '123 Test Street')

class PotentialProductModelTestCase(TestCase):
    def test_create_potential_product(self):
        product = PotentialProduct.objects.create(
            name='Test Product',
            price=9.99,
            url='https://example.com/test-product'
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.url, 'https://example.com/test-product')

class CustomUserCreationFormTestCase(TestCase):
    def test_custom_user_creation_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = CustomUserCreationForm(data)
        self.assertTrue(form.is_valid())

class UserUpdateFormTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_update_form(self):
        data = {
            'username': 'updatedusername',
            'email': 'updated@example.com'
        }
        form = UserUpdateForm(data, instance=self.user)
        self.assertTrue(form.is_valid())

class ProfileUpdateFormTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            staff=self.user,
            phone='1234567890',
            address='123 Test Street'
        )

    def test_profile_update_form(self):
        data = {
            'phone': '0987654321',
            'address': '456 Updated Street'
        }
        form = ProfileUpdateForm(data, instance=self.profile)
        self.assertTrue(form.is_valid())