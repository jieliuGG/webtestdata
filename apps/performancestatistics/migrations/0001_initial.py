# Generated by Django 2.0.5 on 2019-08-01 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeminfoTestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('currentpagetext', models.CharField(default='', help_text='当前页面标识元素text', max_length=100, verbose_name='输入当前页面标识元素text')),
                ('nextpagetext', models.CharField(default='', help_text='下一个页面标识元素text', max_length=100, verbose_name='输入下一个页面标识元素text')),
                ('forcount', models.IntegerField(help_text='用例循环次数', verbose_name='用例循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '内存测试用例',
                'verbose_name_plural': '内存测试用例',
            },
        ),
    ]