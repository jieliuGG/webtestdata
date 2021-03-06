# Generated by Django 2.0.5 on 2019-07-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportname', models.CharField(default='', max_length=100, verbose_name='报告名字')),
                ('reportfile', models.FileField(upload_to='report/%Y%m', verbose_name='报告文件')),
                ('reportimage', models.ImageField(upload_to='report/%Y%m/screenshop/', verbose_name='报告中错误截图')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '报告记录',
                'verbose_name_plural': '报告记录',
            },
        ),
    ]
