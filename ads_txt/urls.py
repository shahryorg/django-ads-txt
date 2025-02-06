from django.conf.urls import url
from ads_txt.views import rules_list, bulk_upload_rules

urlpatterns = [
    url(r'^ads_txt/upload$', bulk_upload_rules, name='ads_txt_bulk_upload'),
    url(r'^ads.txt$', rules_list, name='ads_txt_rule_list'),
]
