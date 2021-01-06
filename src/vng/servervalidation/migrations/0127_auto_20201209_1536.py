# Generated by Django 2.2.13 on 2020-12-09 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0126_auto_20201209_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(blank=True, help_text='The provider run to which this endpoint belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='environment',
            name='test_scenario',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.CASCADE, to='servervalidation.TestScenario'),
        ),
        migrations.AlterField(
            model_name='postmantestresult',
            name='server_run',
            field=models.ForeignKey(help_text='The provider run which this result belongs to', on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='serverheader',
            name='server_run',
            field=models.ForeignKey(blank=True, help_text='The provider run for which this header was used', null=True, on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]
