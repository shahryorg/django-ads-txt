from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from ads_txt.models import Rule

class AdsTxtTest(TestCase):
    def setUp(self):
        self.client = Client()
        Rule.objects.create(
            domain='test.com',
            account_id='121243d',
            account_type='DIRECT',
            authority_id='',
        )

    def test_get_ads_txt(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertIn('test.com', str(response.content))


class UploadAdsTxtTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.password = 'my@password123' 
        self.user = User.objects.create_superuser(
            'admin', 'admin@test.com', self.password)

    def test_bulk_upload_unauthorized(self):
        response = self.client.get(reverse('ads_txt_bulk_upload'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertIn('Log in | Django site admin', str(response.content))

    def test_bulk_upload_get(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('ads_txt_bulk_upload'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.get('content-type'), 'text/html; charset=utf-8')

    def test_bulk_upload_post(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(reverse('ads_txt_bulk_upload'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.get('content-type'), 'text/html; charset=utf-8')