# Generated by Django 5.1.1 on 2024-10-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_job_date_tasks_jobdate_remove_tasks_task_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskjob',
            name='jobname',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='taskdesc',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='typename',
            field=models.CharField(null=True),
        ),
    ]