import django

from django.test import Client, TestCase

from ads_txt.models import Rule
if django.VERSION[:2] >= (2, 0):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


class AdsTxtTest(TestCase):

    def setUp(self):
        self.client = Client()
        Rule.objects.create(domain='test.com',
                            account_id='121243d',
                            account_type='DIRECT',
                            authority_id=''
                            )

    def test_get_ads_txt(self):

        response = self.client.get(reverse('ads_txt_rule_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('test.com', str(response.content))
