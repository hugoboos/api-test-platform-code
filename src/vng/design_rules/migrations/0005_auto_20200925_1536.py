# Generated by Django 2.2.13 on 2020-09-25 13:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('design_rules', '0004_auto_20200925_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='designruleresult',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='designrulesession',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
