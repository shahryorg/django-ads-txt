from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from ads_txt import settings
from ads_txt.models import Rule


class RuleList(ListView):
    model = Rule
    context_object_name = 'rules'
    cache_timeout = settings.CACHE_TIMEOUT

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, request, *args, **kwargs):
        cache_timeout = self.get_cache_timeout()
        super_dispatch = super(RuleList, self).dispatch
        if not cache_timeout:
            return super_dispatch(request, *args, **kwargs)
        cache_decorator = cache_page(cache_timeout, key_prefix="ads_txt_")
        return cache_decorator(super_dispatch)(request, *args, **kwargs)


rules_list = RuleList.as_view()
