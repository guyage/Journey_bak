# Generated by Django 2.0.4 on 2019-03-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_redisdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLInst',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('instname', models.CharField(max_length=128, verbose_name='MySQLInst名称')),
                ('host', models.GenericIPAddressField(verbose_name='MySQLInstIP地址')),
                ('port', models.PositiveIntegerField(verbose_name='MySQLInst端口')),
                ('manageuser', models.CharField(max_length=32, verbose_name='MySQLInst管理用户')),
                ('manageuserpwd', models.CharField(max_length=64, verbose_name='MySQLInst管理用户密码')),
                ('readuser', models.CharField(max_length=32, verbose_name='MySQLInst只读用户')),
                ('readuserpwd', models.CharField(max_length=32, verbose_name='MySQLInst只读用户密码')),
                ('version', models.CharField(default=5.7, max_length=32, verbose_name='MYSQL版本')),
                ('is_enabled', models.PositiveSmallIntegerField(choices=[(0, '禁用'), (1, '启用')], default=1, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': 'MYSQL实例',
                'verbose_name_plural': 'MYSQL实例',
                'db_table': 'mysql_inst',
            },
        ),
        migrations.RemoveField(
            model_name='mysqldatabase',
            name='adminuser',
        ),
        migrations.RemoveField(
            model_name='mysqldatabase',
            name='host',
        ),
        migrations.RemoveField(
            model_name='mysqldatabase',
            name='password',
        ),
        migrations.RemoveField(
            model_name='mysqldatabase',
            name='port',
        ),
        migrations.RemoveField(
            model_name='mysqldatabase',
            name='version',
        ),
        migrations.AddField(
            model_name='mysqldatabase',
            name='service',
            field=models.CharField(blank=True, max_length=128, verbose_name='对应应用'),
        ),
        migrations.AlterField(
            model_name='mongodbinst',
            name='version',
            field=models.CharField(default=5.7, max_length=32, verbose_name='Mongodb版本'),
        ),
        migrations.AddField(
            model_name='mysqldatabase',
            name='mysqlinst_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mysqlinst_id', to='db.MySQLInst', verbose_name='MySQL实例'),
        ),
    ]
