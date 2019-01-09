# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0044_auto_20181218_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exposedurl',
            name='test_session',
        ),
        migrations.AddField(
            model_name='vngendpoint',
            name='test_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsession.TestSession', blank=True, default=None, null=True),
            preserve_default=False,
        ),
    ]