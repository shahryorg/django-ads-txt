from django.contrib.sites.models import Site
from django.core.cache import cache
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
    account_type = models.CharField(_('Account Type'), max_length=100, choices=ACCOUNT_TYPE_CHOICES)
    authority_id = models.CharField(_('Authority ID'), max_length=255, blank=True, null=True)

    sites = models.ManyToManyField(Site, verbose_name=_('sites'), related_name='adstxt')

    class Meta:
        verbose_name = _('rule')
        verbose_name_plural = _('rules')

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
        super(Rule, self).save(*args, **kwargs)
        # invalidate ads.txt cached pages if any
        for entry in cache.keys('*ads_txt_*'):
            cache.delete(entry)
