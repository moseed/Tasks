# Generated by Django 5.1.1 on 2024-10-20 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_curr_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curr_tags',
            name='cur_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.currencies'),
        ),
        migrations.AlterField(
            model_name='curr_tags',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.tags'),
        ),
    ]