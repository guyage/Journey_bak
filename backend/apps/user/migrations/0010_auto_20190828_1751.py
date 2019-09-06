# Generated by Django 2.0.4 on 2019-08-28 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190828_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('f47de2e6-4fed-411f-8753-90d505c2f595'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
