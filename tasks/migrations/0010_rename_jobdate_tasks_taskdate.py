# Generated by Django 5.1.1 on 2024-10-25 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_tasks_jobdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='jobdate',
            new_name='taskdate',
        ),
    ]
