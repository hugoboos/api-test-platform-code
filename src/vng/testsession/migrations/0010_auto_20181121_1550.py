# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-21 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0009_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
