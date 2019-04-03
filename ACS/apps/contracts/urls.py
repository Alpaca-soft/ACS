from django.urls import path

from ACS.apps.contracts.organizations.views import *
from ACS.apps.contracts.status.views import *
from ACS.apps.contracts.views import *


app_name = 'Contracts'

urlpatterns = [

    path('', ContractsItemListView.as_view(), name='contractsList'),
    path('create/', ContractsCreateView.as_view(), name='contractsCreate'),
    path('update/<int:pk>', ContractsUpdateView.as_view(), name='contractsUpdate'),
    path('read/<int:pk>', ContractsReadView.as_view(), name='contractsRead'),
    path('delete/<int:pk>', ContractsDeleteView.as_view(), name='contractsDelete'),

    path('organizations/', OrganizationItemListView.as_view(), name='orgList'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='orgCreate'),
    path('organizations/update/<int:pk>/', OrganizationUpdateView.as_view(), name='orgUpdate'),
    path('organizations/read/<int:pk>/', OrganizationReadView.as_view(), name='orgRead'),
    path('organizations/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='orgDelete'),

    path('status/', StatusListView, name='status'),
    path('status/create/', StatusCreateView.as_view(), name='createStatus'),
    path('status/update/<int:pk>', StatusUpdateView.as_view(), name='updateStatus'),
    path('status/read/<int:pk>', StatusCreateView.as_view(), name='readStatus'),
    path('status/delete/<int:pk>', StatusDeleteView.as_view(), name='deleteStatus'),

]