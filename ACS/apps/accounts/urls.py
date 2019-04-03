from django.urls import path
from ACS.apps.accounts.views import *
from ACS.apps.accounts.personalArea.views import *
from ACS.apps.accounts.contacts.views import changeContacts, ContactView, UsersView

app_name = 'accounts'

urlpatterns = [
    # Регистрация пользователя
    path('register/', register_view, name='register'),
    # Авторизация пользователя
    path('login/', login_view, name='login'),
    # Выход из УЗ
    path('logout/', logout_view, name='logout'),
    # Профиль пользователя
    path('profile/', view_profile, name='profile'),
    path('profile/<int:pk>', view_profile, name='profile_pk'),
    path('profile/edit/', edit_profile, name='editProfile'),
    path('profile/edit/<int:pk>', edit_profile, name='editOutherProfile'),
    path('profile/contacts/', ContactView.as_view(), name='ProfileContacts'),
    path('profile/users/', UsersView.as_view(), name='Users'),
    path('profile/changePassword/', change_password, name='changePassword'),
    path('profile/contact/<str:operation>/<int:pk>', changeContacts, name='changeContact'),
    #url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', changeContacts, name='changeContact')

]
