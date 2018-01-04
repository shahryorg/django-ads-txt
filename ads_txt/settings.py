import sys


class Settings(object):
    defaults = {
        'CACHE_TIMEOUT': ('ADSTXT_CACHE_TIMEOUT', None),
    }

    def __getattr__(self, attribute):
        from django.conf import settings
        if attribute in self.defaults:
            return getattr(settings, *self.defaults[attribute])


sys.modules[__name__] = Settings()
