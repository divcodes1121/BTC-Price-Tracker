# alerts/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Alert

class AlertTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.alert = Alert.objects.create(
            user=self.user,
            cryptocurrency='BTC',
            target_price=30000.00
        )
        self.url = reverse('alert-list')

    def test_create_alert(self):
        data = {
            'cryptocurrency': 'ETH',
            'target_price': 2000.00
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 2)

    def test_list_alerts(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_alert(self):
        url = reverse('alert-detail', args=[self.alert.id])
        response = self.client.delete(url, format='json')
        self.alert.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.alert.status, 'deleted')
