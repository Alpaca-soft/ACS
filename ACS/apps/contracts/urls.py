from django.urls import path

from ACS.apps.contracts.organizations.views import *
from ACS.apps.contracts.status.views import *
from ACS.apps.contracts.views import *


app_name = 'Contracts'

urlpatterns = [
    path('', ContractsItemListView.as_view(), name='contractsList'),
    path('create/', ContractsCreateView.as_view(), name='contractsReader'),
    path('update/<int:pk>', ContractsUpdateView.as_view(), name='contractsUpdate'),
    path('read/<int:pk>', ContractsReadView.as_view(), name='contractsRead'),
    path('delete/<int:pk>', ContractsDeleteView.as_view(), name='contractsDelete'),

    path('org/', OrganizationItemListView.as_view(), name='orgList'),
    path('orgCreate/', OrganizationCreateView.as_view(), name='orgCreate'),
    path('orgUpdate/<int:pk>/', OrganizationUpdateView.as_view(), name='orgUpdate'),
    path('orgRead/<int:pk>/', OrganizationReadView.as_view(), name='orgRead'),
    path('orgDelete/<int:pk>/', OrganizationDeleteView.as_view(), name='orgDelete'),

    path('status/', StatusListView, name='status'),
    path('createStatus/', StatusCreateView.as_view(), name='createStatus'),
    path('updateStatus/<int:pk>', StatusUpdateView.as_view(), name='updateStatus'),
    path('readStatus/<int:pk>', StatusCreateView.as_view(), name='readStatus'),
    path('deleteStatus/<int:pk>', StatusDeleteView.as_view(), name='deleteStatus'),

]