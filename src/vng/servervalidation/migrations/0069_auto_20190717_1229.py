# Generated by Django 2.2.1 on 2019-07-17 10:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0068_auto_20190711_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscenariourl',
            name='placeholder',
            field=models.TextField(blank=True, default='https://www.example.com'),
        ),
    ]