# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse

from cmsplugin_form_handler.forms import FormPluginFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Sample


class SampleForm(FormPluginFormMixin, forms.ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'

    def __init__(self, source_url, instance, **kwargs):
        super(SampleForm, self).__init__(source_url, instance, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': 'novalidate'}
        self.helper.form_action = reverse(
            'cmsplugin_form_handler:process_form', args=(self.plugin_id, ))
        self.helper.add_input(Submit('submit', 'Submit'))
