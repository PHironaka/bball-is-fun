# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-10 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
    ]