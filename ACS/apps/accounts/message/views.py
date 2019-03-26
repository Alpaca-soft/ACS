from django.shortcuts import render, redirect
from django.views import View
from ..models import Chat
from .forms import MessageForm
from django.db.models import Count
from django.urls import reverse
from django import template
from django.contrib import auth
import pytz


register = template.Library()


class DialogsView(View):
    template_name = 'accounts/messages/dialogs.html'

    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])

        content = {
            'title': "1",
            'user_profile': request.user,
            'chats': chats
        }
        #return render(request, 'accounts/messages/dialogs.html', {'user_profile': request.user, 'chats': chats})
        return render(request, self.template_name, content)


@register.simple_tag
def getCompanion(user, chat):
    for users in chat.members.all():
        if users != user:
            return users
    return None


class MessagesView(View):

    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        content = {
            'user_profile': request.user,
            'chat': chat,
            'form': MessageForm()
        }
        return render(request, 'users/messages.html', content)

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat.id}))
