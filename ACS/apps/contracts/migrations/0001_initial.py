# Generated by Django 2.1.7 on 2019-03-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование организации')),
                ('legalAddress', models.TextField(verbose_name='Юредический адрес')),
                ('actualAddress', models.TextField(verbose_name='Фактический адрес')),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('ogrn', models.IntegerField(verbose_name='ОГРН')),
            ],
        ),
    ]
