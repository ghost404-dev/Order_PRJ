from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Order
from django.contrib.auth.models import User

class OrderAPITest(TestCase):
    
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        
        # Логинимся с использованием JWT
        # Получаем JWT токен
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['access']

        # Устанавливаем токен в заголовки для всех запросов
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_order(self):
        """Тест на создание заказа"""
        data = {
            "project_name": "Test Project",
            "description": "Test Description",
            "status": "new",
            "client": "Client Name",
            "deadline": "2024-12-31",
        }
        response = self.client.post('/api/orders/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().project_name, 'Test Project')

    def test_get_orders(self):
        """Тест на получение списка заказов"""
        # Создаем тестовые заказы
        Order.objects.create(project_name='Test Project 1', client='Client 1', status='new', deadline='2024-12-31')
        Order.objects.create(project_name='Test Project 2', client='Client 2', status='in_progress', deadline='2024-12-31')

        response = self.client.get('/api/orders/', format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_order(self):
        """Тест на обновление заказа"""
        order = Order.objects.create(project_name='Old Project', client='Client 1', status='new', deadline='2024-12-31')
        data = {
            "project_name": "Updated Project",
            "description": "Updated Description",
            "status": "in_progress",
            "client": "Updated Client",
            "deadline": "2025-01-01",
        }
        response = self.client.put(f'/api/orders/{order.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.project_name, 'Updated Project')
        self.assertEqual(order.status, 'in_progress')

    def test_delete_order(self):
        """Тест на удаление заказа"""
        order = Order.objects.create(project_name='Project to Delete', client='Client 1', status='new', deadline='2024-12-31')
        
        response = self.client.delete(f'/api/orders/{order.id}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

