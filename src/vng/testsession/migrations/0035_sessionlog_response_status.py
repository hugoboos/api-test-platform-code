# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0034_auto_20181217_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionlog',
            name='response_status',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
