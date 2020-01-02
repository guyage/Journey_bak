# Generated by Django 2.0.4 on 2019-12-19 02:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20191219_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('f164088f-c397-4496-9cbd-c78957d56b1b'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
