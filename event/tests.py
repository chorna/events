from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class RoomTests(APITestCase):
    def test_create_room(self):
        url = reverse('room_create')
        data = {'name': 'new room', 'capacity': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': int(response.data['id']), 'name': 'new room', 'capacity': 100})

        data2 = {'name': 'new room 2', 'capacity': 100}
        response = self.client.post(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_room(self):
        url = reverse('room_create')
        data = {'name': 'new room', 'capacity': 100}
        response = self.client.post(url, data, format='json')

        url_delete = reverse('room_delete', kwargs={'pk': int(response.data['id'])})
        response2 = self.client.delete(url_delete)
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)

        data3 = {'name': 'new room', 'capacity': 100}
        response3 = self.client.post(url, data3, format='json')

        url_event = reverse('event_create')
        data4 = {'name': 'new event', 'capacity': 50, 'room': int(response3.data['id']), 'type':1, 'date': '2022-08-20'}
        response4 = self.client.post(url_event, data4, format='json')
        self.assertEqual(response4.status_code, status.HTTP_201_CREATED)

        url_delete = reverse('room_delete', kwargs={'pk': int(response3.data['id'])})
        response5 = self.client.delete(url_delete)
        self.assertEqual(response5.status_code, status.HTTP_400_BAD_REQUEST)

    def test_capacity(self):
        url = reverse('room_create')
        data = {'name': 'new room', 'capacity': 100}
        response = self.client.post(url, data, format='json')

        url_event = reverse('event_create')
        data2 = {'name': 'new event', 'capacity': 150, 'room': int(response.data['id']), 'type':1, 'date': '2022-08-20'}
        response2 = self.client.post(url_event, data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

        data3 = {'name': 'new event', 'capacity': 50, 'room': int(response.data['id']), 'type':1, 'date': '2022-08-20'}
        response3 = self.client.post(url_event, data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)