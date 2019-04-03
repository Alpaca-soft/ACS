from django import forms

from pagedown.widgets import PagedownWidget
from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from ACS.apps.contracts.organizations.forms import *
from ACS.apps.contracts.models import *


class ContractsForms(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Contracts
        fields = [

        ]
