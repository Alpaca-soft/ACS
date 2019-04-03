from ACS.apps.contracts.status.models import *
from ACS.apps.contracts.status.forms import StatusForm, SexForm

from django.db.models import Q
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


# Пагинация

class StatusItemListView(ListView):
    template_name = 'status/marks/statusList.html'

    def get(self, request):
        if request.user.is_superuser:
            queryset_list = Status.objects.all()
        else:
            raise Http404

        return render(
            request=request,
            template_name=self.template_name,
            context=
            {
                "title": "[LIS]: Управление статусами",
                'object_list': get_paginated_page(request, queryset_list),
            })

    def post(self, request):
        if request.is_ajax():
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='status/marks/statusList.html',
                    context={'object_list': get_paginated_page(request, Status.objects.all())}
                )
            })
        else:
            raise Http404()


def get_paginated_page(request, objects, number=10):
    current_page = Paginator(objects, number)
    page = request.GET.get('page') if request.method == 'GET' else request.POST.get('page')
    try:
        return current_page.page(page)
    except PageNotAnInteger:
        return current_page.page(1)
    except EmptyPage:
        return current_page.page(current_page.num_pages)


# ==== Status
class StatusCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'lib/LibLis/modals/statusCreate.html'
    form_class = StatusForm
    success_message = 'Читатель успешно создан.'
    success_url = reverse_lazy('lib:list')


# Update
class StatusUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Status
    template_name = 'status/marks/statusUpdate.html'
    form_class = StatusForm
    success_message = 'Данные читателя были успешно отредактированы и сохранены.'
    success_url = reverse_lazy('lib:list')


# Sigles
class StatusReadView(generic.DetailView):
    model = Status
    form_class = StatusForm
    template_name = 'status/marks/statusRead.html'


# Delete
class StatusDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Status
    template_name = 'status/marks/statusDelete.html'
    success_message = 'Читатель был удалён.'
    success_url = reverse_lazy('lib:list')


class StatusListView(ListView):
    model = Status
    template_name = 'status/marks/statusList.html'


class StatusViewSiglesForm:
    today = timezone.now().date()
    model = Status


# ==== Sex

class SexCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'lib/LibLis/modals/create_sigles.html'
    form_class = SexForm
    success_message = 'Читатель успешно создан.'
    success_url = reverse_lazy('lib:list')


# Update
class SexUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Sex
    template_name = 'lib/LibLis/modals/update_reader.html'
    form_class = SexForm
    success_message = 'Данные читателя были успешно отредактированы и сохранены.'
    success_url = reverse_lazy('lib:list')


# Sigles
class SexReadView(generic.DetailView):
    model = Sex
    form_class = SexForm
    template_name = 'lib/LibLis/modals/read_reader.html'


# Delete
class SexDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Sex
    template_name = 'lib/LibLis/modals/delete_reader.html'
    success_message = 'Читатель был удалён.'
    success_url = reverse_lazy('lib:list')


class SexListView(ListView):
    model = Sex
    modelSex = Status
    #context_object_name = '[LIS]: Управление статусами'
    template_name = 'lib/LibLis/status/statusList.html'


class SexSiglesForm:
    today = timezone.now().date()
    model = Sex
