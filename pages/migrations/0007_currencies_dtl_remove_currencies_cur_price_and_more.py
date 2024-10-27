# Generated by Django 5.1.2 on 2024-10-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_currencyprice_cur_id_currencies_cur_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies_dtl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('desc', models.CharField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='currencies',
            name='cur_price',
        ),
        migrations.AddField(
            model_name='currencies',
            name='cur_dtl',
            field=models.ManyToManyField(to='pages.currencies_dtl'),
        ),
    ]
