# Generated by Django 2.0.5 on 2019-07-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportrecord', '0012_auto_20190704_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reportname',
            field=models.CharField(default='', max_length=100, verbose_name='测试执行开始时间串'),
        ),
    ]
