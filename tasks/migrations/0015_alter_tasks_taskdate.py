# Generated by Django 5.1.1 on 2024-10-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_tasks_taskdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskdate',
            field=models.DateField(),
        ),
    ]
