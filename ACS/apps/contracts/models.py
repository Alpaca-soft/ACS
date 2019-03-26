from django.db import models

# Create your models here.

from ACS.apps.contracts.organizations.models import *


class ContractsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ContractsManager, self)


class Contracts(models.Model):
    govContract = models.CharField(max_length=255, verbose_name="Гос. контракт")
    creationDate = models.DateTimeField(auto_now_add=True)
    startContract = models.DateField(verbose_name="Действие контракта с")
    stopContract = models.DateField(verbose_name="Дата окончания контракта")
    openContract = models.BooleanField(verbose_name="Закрыть контракт")
    residue = models.FloatField(verbose_name="Остаток")
    #расчетный счет
