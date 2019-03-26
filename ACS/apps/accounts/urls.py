from django.urls import path
from ACS.apps.accounts.views import *
from ACS.apps.accounts.personalArea.views import *
from ACS.apps.accounts.contacts.views import changeContacts, ContactView, UsersView

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('profile/', view_profile, name='profile'),
    path('profile/<int:pk>', view_profile, name='profile_pk'),
    path('profile/edit/', edit_profile, name='editProfile'),
    path('profile/edit/<int:pk>', edit_profile, name='editOutherProfile'),
    path('profile/contacts/', ContactView.as_view(), name='ProfileContacts'),
    path('users/', UsersView.as_view(), name='Users'),
    path('changePassword/', change_password, name='changePassword'),
    path('contact/<str:operation>/<int:pk>', changeContacts, name='changeContact'),
    #url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', changeContacts, name='changeContact')
]
