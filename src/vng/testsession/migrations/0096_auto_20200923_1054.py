# Generated by Django 2.2.13 on 2020-09-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0095_auto_20191018_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vngendpoint',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
    ]
