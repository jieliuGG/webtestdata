# Generated by Django 2.0.5 on 2019-04-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmerchant', '0003_auto_20190415_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmerchant',
            name='isfictitious',
            field=models.BooleanField(default=False, verbose_name='是否虚拟商户'),
        ),
    ]
