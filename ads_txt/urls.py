from django.conf.urls import url

from ads_txt.views import rules_list

urlpatterns = [
    url(r'^$', rules_list, name='ads_txt_rule_list'),
]
