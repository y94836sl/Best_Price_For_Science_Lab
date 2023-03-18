from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Product, Order, PotentialProduct
from .forms import ProductForm, OrderForm

User = get_user_model()

class InventoryModelTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            category='Stationary',
            quantity=5,
            price=9.99,
            url='https://example.com'
        )
        
    def test_create_product(self):
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

    def test_create_order(self):
        order = Order.objects.create(
            product=self.product,
            staff=self.user,
            order_quantity=2
        )
        order_count = Order.objects.count()
        self.assertEqual(order_count, 1)

class InventoryFormTests(TestCase):

    def test_product_form_valid(self):
        form = ProductForm(data={
            'name': 'Test Product',
            'category': 'Stationary',
            'quantity': 5,
            'price': 9.99,
            'url': 'https://example.com'
        })
        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        form = ProductForm(data={
            'name': '',
            'category': 'Stationary',
            'quantity': 5,
            'price': 9.99,
            'url': 'https://example.com'
        })
        self.assertFalse(form.is_valid())

class InventoryViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_dashboard_view_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/accounts/login/?next=' + reverse('dashboard'))

    def test_dashboard_view_authorized_access(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
