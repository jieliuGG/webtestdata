# Generated by Django 2.0.5 on 2019-07-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportrecord', '0004_auto_20190704_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='对比图片'),
        ),
    ]
