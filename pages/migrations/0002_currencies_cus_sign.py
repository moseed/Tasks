# Generated by Django 5.1.1 on 2024-10-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencies',
            name='cus_sign',
            field=models.TextField(null=True),
        ),
    ]