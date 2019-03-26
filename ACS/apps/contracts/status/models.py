from django.db import models


# Статус читателя
class Status(models.Model):
    readerStatus = models.CharField(max_length=50, verbose_name='Статус читателя')

    class Meta:
        verbose_name = 'Статус читателя'
        verbose_name_plural = 'Стутус читателя'

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.status

    pass


# Пол читателя
class Sex(models.Model):
    gender = models.CharField(max_length=25, verbose_name='Пол:')

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __unicode__(self):
        return self.gender

    def __str__(self):
        return self.gender

    pass
