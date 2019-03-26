from django.db import models

# Create your models here.

class ContractsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ContractsManager, self)


class OrganizationInfo(models.Model):
    inn = models.BigIntegerField(verbose_name="ИНН")
    ogrn = models.BigIntegerField(verbose_name="ОГРН")
    kpp = models.BigIntegerField(verbose_name="КПП")
    oktmo = models.BigIntegerField(verbose_name="ОКТМО")


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Контрагент")
    legalAddress = models.TextField(verbose_name="Юредический адрес")
    actualAddress = models.TextField(verbose_name="Фактический адрес")
