from django.urls import path

from ACS.apps.Lib.LisLib.schools.views import *
from ACS.apps.Lib.LisLib.sigles.views import *
from ACS.apps.Lib.LisLib.readers.views import *
from ACS.apps.Lib.LisLib.status.views import *

app_name = 'contractors'

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('create/', ReaderCreateView.as_view(), name='create_reader'),
    path('update/<int:pk>', ReaderUpdateView.as_view(), name='update_reader'),
    path('read/<int:pk>', ReaderReadView.as_view(), name='read_reader'),
    path('delete/<int:pk>', ReaderDeleteView.as_view(), name='delete_reader'),

    path('sigles/', SiglesItemListView.as_view(), name='sigles'),
    path('createSigles/', SiglesCreateView.as_view(), name='create_sigles'),
    path('updateSigles/<int:pk>/', SiglesUpdateView.as_view(), name='update_sigles'),
    path('readSigles/<int:pk>/', SiglesReadView.as_view(), name='read_sigles'),
    path('deleteSigles/<int:pk>/', SiglesDeleteView.as_view(), name='delete_sigles'),

    path('school/', SchoolItemListView.as_view(), name='school'),
    path('createSchool/', SchoolCreateView.as_view(), name='create_schools'),
    path('updateSchool/<int:pk>',SchoolUpdateView.as_view(), name='update_schools'),
    path('readSchool/<int:pk>', SchoolReadView.as_view(), name='read_schools'),
    path('deleteSchool/<int:pk>', SchoolDeleteView.as_view(), name='delete_schools'),



    #path('', views.Index.as_view(), name='index'),
    path('status/', StatusListView,  name='status'),
    path('createStatus/', StatusCreateView.as_view(), name='createStatus'),
    path('createSex/', SexCreateView.as_view(), name='createSex'),
    path('updateStatus/<int:pk>', StatusUpdateView.as_view(), name='updateStatus'),
    path('updateSex/<int:pk>', SexUpdateView.as_view(), name='updateSex'),
    path('readStatus/<int:pk>', StatusCreateView.as_view(), name='readStatus'),
    path('readSex/<int:pk>', SexReadView.as_view(), name='readSex'),
    path('deleteStatus/<int:pk>', StatusDeleteView.as_view(), name='deleteStatus'),
    path('deleteSex/<int:pk>', SexDeleteView.as_view(), name='deleteSex'),

]
