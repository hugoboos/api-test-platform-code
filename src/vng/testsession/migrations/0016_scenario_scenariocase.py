# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-10 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0015_auto_20181205_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('application', models.CharField(max_length=200, null=True)),
                ('version', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('performed', models.DateTimeField(blank=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsession.Session')),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, null=True, unique=True)),
                ('result', models.CharField(choices=[('Succesvol', 'success'), ('Niet succesvol', 'failed'), ('Niet uitgevoerd', 'not called')], default='Niet uitgevoerd', max_length=20)),
            ],
        ),
    ]
