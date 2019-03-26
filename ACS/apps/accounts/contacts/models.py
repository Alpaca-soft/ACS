from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='Владелец', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_contact(cls, current_user, new_contact):
        contact, created = cls.objects.get_or_create(current_user=current_user)
        contact.users.add(new_contact)

    @classmethod
    def lose_contact(cls, current_user, new_contact):
        contact, created = cls.objects.get_or_create(current_user=current_user)
        contact.users.remove(new_contact)
