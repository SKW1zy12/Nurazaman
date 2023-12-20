# Generated by Django 5.0 on 2023-12-20 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('logo_complex', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='whatsapp URL')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='instagram URL')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='facebook URL')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='SettingsPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_title', to='base.settings')),
            ],
            options={
                'unique_together': {('settings', 'phone')},
            },
        ),
    ]
