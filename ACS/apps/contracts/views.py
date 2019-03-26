from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.views.generic import ListView
from django.template.loader import render_to_string
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin

from ACS.apps.contracts.models import Organization, Contracts
from ACS.apps.contracts.forms import ContractsForms

# Create your views here.
from ACS.apps.contracts.models import Organization


class ContractsItemListView(ListView):
    template_name = 'contracts/organizations/orgList.html'

    def get(self, request):
        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Contracts.objects.all()
        else:
            raise Http404

        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(rdr_id__icontains=query) |
                Q(name__icontains=query)
            ).distinct()

        return render(
            request=request,
            template_name=self.template_name,
            context=
            {
                "title": "[ACS]: Контракты",
                'object_list': get_paginated_page(request, queryset_list),
            })

    def post(self, request):
        if request.is_ajax():
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='contracts/organizations/orgList.html',
                    context={'object_list': get_paginated_page(request, Contracts.objects.all())}
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


# Create
class ContractsCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'lib/LibLis/modals/create_reader.html'
    form_class = ContractsForms
    success_message = 'Читатель успешно создан.'
    success_url = reverse_lazy('LibLib:list')


# Update
class ContractsUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Contracts
    template_name = 'lib/LibLis/modals/update_reader.html'
    form_class = ContractsForms
    success_message = 'Данные читателя были успешно отредактированы и сохранены.'
    success_url = reverse_lazy('LibLib:list')


# Read
class ContractsReadView(generic.DetailView):
    model = Contracts
    form_class = ContractsForms
    template_name = 'lib/LibLis/modals/read_reader.html'


# Delete
class ContractsDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Contracts
    template_name = 'lib/LibLis/modals/delete_reader.html'
    success_message = 'Читатель был удалён.'
    success_url = reverse_lazy('LibLib:list')


class ContractsListView(ListView):
    model = Contracts
    template_name = 'lib/LibLis/readers_list.html'


class ViewContractsForm:
    today = timezone.now().date()
    model = Contracts
