from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Restaurant

# Create your tests here.
class RestaurantListCreation(TestCase):

    def setUp(self):
        self.client = Client()
        self.restaurant_1 = {
            'manager': 'test_manager',
            'manager_phone': '123456789256',
            'manager_email': 'manager@manager.exa',
            'name': 'chepo aguilar',
            'location': 'wework',
            'phone': '124568792358',
            'picture': 'https://www.google.com.mx/imgres?imgurl'
        }

    def test_post_restaurant(self):
        data = {
                    'manager': 'test_manager',
                    'manager_phone': '123456789256',
                    'manager_email': 'manager@manager.exa',
                    'name': 'chepo aguilar',
                    'location': 'wework',
                    'phone': '124568792358',
                    'picture': 'https://www.google.com.mx/imgres?imgurl'
                }
        response = self.client.post(
            reverse('restaurants:create_list'),
            data=json.dumps(data),
            content_type='application/json'
        )

        response_content = json.loads(response.content.decode('utf-8'))
        shared_items = set(data.items()) & set(response_content.items())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(shared_items), 7)

    def test_restaurant_get(self):
        response = self.client.get(
            reverse('restaurants:create_list')
        )
        self.assertEqual(response.status_code, 200)


class RestaurantUpdateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.restaurant_1 = Restaurant.objects.create(
            manager= 'test_manager',
            manager_phone= '123456789256',
            manager_email= 'manager@manager.exa',
            name= 'chepo aguilar',
            location= 'wework',
            phone= '124568792358',
            picture= 'https://www.google.com.mx/imgres?imgurl'
        )

    def test_get_single_restaurant(self):
        response = self.client.get(
            reverse('restaurants:update', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 200)
        
    def test_patch_single_restaurant(self):
        response = self.client.patch(
            reverse('restaurants:update', kwargs={'pk': 1}),
            data=json.dumps({'name': 'Toni la espaniola'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        

    def test_patch_error_single_restaurant(self):
        response = self.client.patch(
            reverse('restaurants:update', kwargs={'pk': 1}),
            data=json.dumps({'phone': '123454987654676564646846'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_put_single_restaurant(self):
        response = self.client.put(
            reverse('restaurants:update', kwargs={'pk': 1}),
            data=json.dumps(
                {
                    'manager': 'test_manager',
                    'manager_phone': '123456789256',
                    'manager_email': 'manager@manager.exa',
                    'name': 'chepo aguilar',
                    'location': 'wework',
                    'phone': '124568792358',
                    'picture': 'https://www.google.com.mx/imgres?imgurl'
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
    def test_put_error_single_restaurant(self):
        response = self.client.put(
            reverse('restaurants:update', kwargs={'pk': 1}),
            data=json.dumps({'phone': '123454987654676564646846'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_restaurant(self):
        response = self.client.delete(
            reverse('restaurants:update', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 204)

    def test_error_delete_restaurant(self):
        response = self.client.delete(
            reverse('restaurants:update', kwargs={'pk': 100})
        )
        self.assertEqual(response.status_code, 404)