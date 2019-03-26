from django import forms
from ACS.apps.contracts.status.models import Sex, Status
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class StatusForm(PopRequestMixin,CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            "readerStatus"
        ]


class SexForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Sex
        fields = [
            "gender"
        ]
