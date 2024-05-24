from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.views.generic.edit import FormView

from ads_txt import settings
from ads_txt.models import Rule


class RuleList(ListView):
    model = Rule
    context_object_name = 'rules'
    cache_timeout = settings.CACHE_TIMEOUT
    content_type = 'text/plain'

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, request, *args, **kwargs):
        cache_timeout = self.get_cache_timeout()
        super_dispatch = super(RuleList, self).dispatch
        if not cache_timeout:
            return super_dispatch(request, *args, **kwargs)
        cache_decorator = cache_page(cache_timeout)
        return cache_decorator(super_dispatch)(request, *args, **kwargs)

from django import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class BulkRulesForm(forms.Form):

    ads_rules = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        ads_rules = cleaned_data.get('ads_rules')

        matches, errors = [], []
        for index, rule in enumerate(
                ads_rules.splitlines(keepends=False), start=1):

            if not rule.strip():
                continue

            match = Rule.validate(rule.strip())
            if not match:
                errors.append(str(index))
                continue

            matches.append(match.groupdict())

        if errors:
            raise forms.ValidationError(_('Error reading lines:\n') + ',\n'.join(errors))

        cleaned_data['ads_rules'] = matches
        return cleaned_data

@method_decorator(staff_member_required, name='dispatch')
class UploadRulesFormView(FormView):
    template_name = "ads_txt/change_form.html"
    form_class = BulkRulesForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        ads_list = form.cleaned_data.get('ads_rules')
        for ads_dict in ads_list:
            Rule.objects.get_or_create(**ads_dict)

        messages.add_message(self.request, messages.SUCCESS, _('ads.txt rules updated with success'))
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Failed to update ads.txt'))
        return self.render_to_response(self.get_context_data(form=form))

rules_list = RuleList.as_view()
bulk_upload_rules = UploadRulesFormView.as_view()
