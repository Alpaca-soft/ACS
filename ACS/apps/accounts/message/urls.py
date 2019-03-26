from django.urls import path
from .views import DialogsView, MessagesView, CreateDialogView


urlpatterns = [
    path('', DialogsView.as_view(), name='dialogs'),
    path('create/<int:pk>', CreateDialogView.as_view(), name='create_dialog'),
    path('<int:pk>', MessagesView.as_view(), name='messages'),
]
