import re
from django.contrib.sites.models import Site
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Rule(models.Model):

    DIRECT = 'DIRECT'
    RESELLER = 'RESELLER'

    ACCOUNT_TYPE_CHOICES = (
        (DIRECT, 'DIRECT'),
        (RESELLER, 'RESELLER')
    )

    domain = models.CharField(_('Domain'), max_length=100)
    account_id = models.CharField(_('account ID'), max_length=255)
    account_type = models.CharField(_('Account Type'), max_length=100, choices=ACCOUNT_TYPE_CHOICES,)
    authority_id = models.CharField(_('Authority ID'), max_length=255, blank=True, null=True)

    sites = models.ManyToManyField(Site, verbose_name=_('sites'), related_name='adstxt')

    class Meta:
        verbose_name = _('rule')
        verbose_name_plural = _('rules')

    def __str__(self):
        return self.domain

    @staticmethod
    def validate(line):
        """
            Specs:
            https://iabtechlab.com/wp-content/uploads/2019/03/IAB-OpenRTB-Ads.txt-Public-Spec-1.0.2.pdf
        """
        # TODO: This regex does not support:
        # 3.4.1 Comments, 3.5 Variables, 4.4 Contact Records, 4.5 Subdomain Referral, etc ...
        pattern = r'(?P<domain>.+),\s*(?P<account_id>.+),\s*(?P<account_type>RESELLER|DIRECT)(,\s*(?P<authority_id>.+))?'
        return re.search(pattern, line)
