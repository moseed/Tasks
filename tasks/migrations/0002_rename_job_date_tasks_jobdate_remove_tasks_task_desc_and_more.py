# Generated by Django 5.1.1 on 2024-10-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='job_date',
            new_name='jobdate',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='task_desc',
        ),
        migrations.AddField(
            model_name='taskjob',
            name='jobstatus',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='typestatus',
            field=models.BooleanField(null=True),
        ),
    ]
