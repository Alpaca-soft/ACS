from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.views.generic import ListView
from django.template.loader import render_to_string
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin

from ACS.apps.contracts.organizations.models import Organization
from ACS.apps.contracts.organizations.forms import OrganizationForms

# Create your views here.


class OrganizationItemListView(ListView):
    template_name = 'contracts/organizations/orgList.html'

    def get(self, request):
        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Organization.objects.all()
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
                "title": "[ACS]: Организации",
                'object_list': get_paginated_page(request, queryset_list),
            })

    def post(self, request):
        if request.is_ajax():
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='contracts/organizations/orgList.html',
                    context={'object_list': get_paginated_page(request, Organization.objects.all())}
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
class OrganizationCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'contracts/organizations/orgCreate.html'
    form_class = OrganizationForms
    success_message = 'Читатель успешно создан.'
    success_url = reverse_lazy('LibLib:list')


# Update
class OrganizationUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Organization
    template_name = 'contracts/organizations/orgUpdate.html'
    form_class = OrganizationForms
    success_message = 'Данные читателя были успешно отредактированы и сохранены.'
    success_url = reverse_lazy('LibLib:list')


# Read
class OrganizationReadView(generic.DetailView):
    model = Organization
    form_class = OrganizationForms
    template_name = 'contracts/organizations/orgView.html'


# Delete
class OrganizationDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Organization
    template_name = 'contracts/organizations/orgDelete.html'
    success_message = 'Читатель был удалён.'
    success_url = reverse_lazy('LibLib:list')


class OrganizationListView(ListView):
    model = Organization
    template_name = 'contracts/organizations/orgList.html'


class ViewOrganizationForm:
    today = timezone.now().date()
    model = Organization
