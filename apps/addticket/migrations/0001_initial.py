# Generated by Django 2.0.5 on 2019-05-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('ffzt', models.CharField(blank=True, default='', help_text='1表示开启，否则为关闭', max_length=100, null=True, verbose_name='输入发放状态的单选的内容')),
                ('kcslinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入库存数量的内容')),
                ('qyxq', models.CharField(blank=True, default='', help_text='1表示相对时间，否则为绝对时间', max_length=100, null=True, verbose_name='输入券有效期的选项的内容')),
                ('xdsjtsinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入券有效期选择相对时间时相对天数的内容')),
                ('yxcbcdf', models.CharField(blank=True, default='', help_text='1表示平台，否则为商户', max_length=100, null=True, verbose_name='输入营销成本承担方的单选内容')),
                ('yhqmcinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入优惠券名称的内容')),
                ('yhlx', models.CharField(blank=True, default='', help_text='1表示代金券', max_length=100, null=True, verbose_name='输入优惠类型的选项的内容')),
                ('yhms', models.CharField(blank=True, default='', help_text='1表示固定金额，否则为随机金额', max_length=100, null=True, verbose_name='输入优惠模式的选项的内容')),
                ('gdjemzinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入固定金额的面值的内容')),
                ('sjjemzmiminputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入随机金额的面值的最小值的内容')),
                ('sjjemzmimaxinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入随机金额的面值的最大值的内容')),
                ('zdxfinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入最低消费的内容')),
                ('sypt', models.CharField(blank=True, default='', help_text='0表示两个都点选，1表示点选QRindo，为2表示点选PaySDK', max_length=100, null=True, verbose_name='输入使用平台的复选的内容')),
                ('syfw', models.CharField(blank=True, default='', help_text='1表示不限，为2表示指定行业，为3表示指定商户', max_length=100, null=True, verbose_name='输入使用范围的选项的内容')),
                ('zdhyoptionxpath', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='输入指定行业的选项的xpath的内容')),
                ('zdshinputtext', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入指定商户的商户名称或ID的内容')),
                ('isplsh', models.BooleanField(default=False, verbose_name='是否使用批量导入商户功能')),
                ('plfilepath', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='输入导入批量商户的文件的路径')),
                ('sfzctq', models.CharField(blank=True, default='', help_text='1表示可退，为2表示不可退', max_length=100, null=True, verbose_name='输入是否支持退券的单选的内容')),
                ('iscancel', models.BooleanField(default=False, verbose_name='是否点击取消按钮')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '添加活动测试数据',
                'verbose_name_plural': '添加活动测试数据',
            },
        ),
    ]