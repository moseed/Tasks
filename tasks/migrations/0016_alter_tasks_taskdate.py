# Generated by Django 5.1.1 on 2024-10-28 19:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_tasks_taskdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
