# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatapp',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
