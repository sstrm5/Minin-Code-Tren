# Generated by Django 5.1 on 2024-09-28 17:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('phone', models.CharField(help_text='Уникальный номер телефона для каждого пользователя', max_length=20, unique=True, verbose_name='Номер телефона')),
                ('token', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='Токен авторизации')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]