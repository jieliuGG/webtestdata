# Generated by Django 2.0.5 on 2019-01-21 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pageelement', '0007_auto_20190121_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eletestdata',
            name='projectmodule',
        ),
        migrations.RemoveField(
            model_name='eletestdata',
            name='testproject',
        ),
    ]
