# Generated by Django 2.2.4 on 2019-11-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0099_auto_20191108_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api',
            options={'permissions': (('list_scenario_for_api', 'View the list of test scenarios for this API'), ('create_scenario_for_api', 'Create a test scenario for this API'), ('update_scenario_for_api', 'Update a test scenario for this API'), ('delete_scenario_for_api', 'Delete a test scenario for this API'), ('update_environment_for_api', 'Update an environment for this API'))},
        ),
    ]