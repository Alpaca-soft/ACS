from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
'''

class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = ((DIALOG, 'Dialog'), (CHAT, 'Chat'))

    type = models.CharField(verbose_name='Тип', max_length=1, choices=CHAT_TYPE_CHOICES,  default=DIALOG)
    members = models.ManyToManyField(User, verbose_name="Участник")

    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk}


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    pubDate = models.DateTimeField(verbose_name='Дата сообщения', default=timezone.now)
    isReaded = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
'''