from django.test import TestCase, Client
from django.urls import reverse
import os

class AuthViewsTestCase(TestCase):
    def setUp(self):
        pass

    def test_login_patient_view(self):
        client = Client()
        url = reverse('login_patient')
        response = client.post(url, {'username': f'{os.getenv("PATIENT")}', 'password': f'{os.getenv("PASSWORD")}'})


        json_data = response.json()
        self.assertEqual(json_data.get('status'), 'success')

        self.assertEqual(client.session['user_id'], 8)
        self.assertEqual(client.session['name'], 'Mr Tladi')
        self.assertTrue(client.session['is_authenticated'])

    def test_login_doctor_view(self):
        client = Client()
        url = reverse('login_doctor')
        response = client.post(url, {'username': f'{os.getenv("DOCTOR")}', 'password': f'{os.getenv("PASSWORD")}'})


        json_data = response.json()
        self.assertEqual(json_data.get('status'), 'success')

        self.assertEqual(client.session['user_id'], 10)
        self.assertEqual(client.session['name'], 'Dr Spies')
        self.assertTrue(client.session['is_authenticated'])

    def test_login_admin_view(self):
        client = Client()
        url = reverse('login_admin')
        response = client.post(url, {'username': f'{os.getenv("ADMIN")}', 'password': f'{os.getenv("PASSWORD")}'})


        json_data = response.json()
        self.assertEqual(json_data.get('status'), 'success')
        

        self.assertEqual(client.session['user_id'], 2)
        self.assertEqual(client.session['name'], 'Admin User')
        self.assertTrue(client.session['is_authenticated'])

    def test_logout_view(self):
        client = Client()
        
        url = reverse('login_patient')
        response = client.post(url, {'username': f'{os.getenv("PATIENT")}', 'password': f'{os.getenv("PASSWORD")}'})
        

        json_data = response.json()
        self.assertEqual(json_data.get('status'), 'success')
        
        # 2nd Request
        
        url = reverse('logout')

        response = client.post(url)

        json_data = response.json()
        self.assertEqual(json_data.get('status'), 'success')

        self.assertNotIn('user_id', self.client.session)
        self.assertNotIn('access_token', self.client.session)
        self.assertNotIn('token_type', self.client.session)
        self.assertNotIn('is_authenticated', self.client.session)
        self.assertNotIn('name', self.client.session)
