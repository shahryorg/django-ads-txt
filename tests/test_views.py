from django.urls import reverse_lazy
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
        response = self.client.get(
            reverse_lazy('ads_txt_bulk_upload'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html;', response.get('content-type'))
        self.assertContains(response, 'Log in | Django site admin')

    def test_bulk_upload_get(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(
            reverse_lazy('ads_txt_bulk_upload'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html;', response.get('content-type'))

    def test_bulk_upload_post(self):

        data = {'ads_rules': '\n'.join([
            "test.com, 121243d, DIRECT",
            "test.com, re121243d, RESELLER, re121243d"])
        }

        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(
            reverse_lazy('ads_txt_bulk_upload'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html;', response.get('content-type'))
        self.assertContains(response, 'rules updated with success')

    def test_bulk_upload_post_invalid(self):

        data = {'ads_rules': '\n'.join([
            "test.com121243d, DIRECT",
            "test.com, re121243d, RESELLER, re121243d\r\n",
            "\r\n",
            "test.com, re121243d, re121243d"
            "\n"])
        }

        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(
            reverse_lazy('ads_txt_bulk_upload'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to update')
        self.assertContains(response, 'Error reading lines')