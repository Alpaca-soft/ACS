from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import Contact
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'accounts/contacts/contact.html'

    def get(self, request):

        users = User.objects.exclude(id=request.user.id)
        try:
            contact = Contact.objects.get(current_user=request.user)
            contacts = contact.users.all()

        except Contact.DoesNotExist:
            contacts = None

        content = {
            'users': users,
            'title': 'Мои контакты',
            'contacts': contacts
        }
        return render(request, self.template_name, content)


class UsersView(TemplateView):
    template_name = 'accounts/contacts/users.html'

    def get(self, request):

        users = User.objects.exclude(id=request.user.id)

        try:
            contact = Contact.objects.get(current_user=request.user)
            contacts = contact.users.all()

        except Contact.DoesNotExist:
            contacts = None

        content = {
            'users': users,
            'title': 'Пользователи портала',
            'contacts': contacts
        }
        return render(request, self.template_name, content)


def changeContacts(request, operation, pk):
    contact = User.objects.get(pk=pk)

    if operation == 'add':
        Contact.make_contact(request.user, contact)
        return redirect('accounts:Users')

    elif operation == 'remove':
        Contact.lose_contact(request.user, contact)
        return redirect('accounts:ProfileContacts')
