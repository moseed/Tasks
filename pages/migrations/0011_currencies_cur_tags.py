# Generated by Django 5.1.1 on 2024-10-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_remove_currencies_cur_dtl'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencies',
            name='cur_tags',
            field=models.ManyToManyField(to='pages.tags'),
        ),
    ]