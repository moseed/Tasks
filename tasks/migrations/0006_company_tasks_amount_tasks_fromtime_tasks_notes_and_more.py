# Generated by Django 5.1.1 on 2024-10-25 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_tasks_jobdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField()),
                ('comp_name_e', models.CharField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tasks',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='fromtime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='teamviwer',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='totime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='version',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='comp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.company'),
        ),
    ]
