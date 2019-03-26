from django import forms

from pagedown.widgets import PagedownWidget
from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from ACS.apps.contracts.organizations.models import *


class OrganizationForms(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Organization
        fields = [

        ]
