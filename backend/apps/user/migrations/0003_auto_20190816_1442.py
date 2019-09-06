# Generated by Django 2.0.4 on 2019-08-16 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190813_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='component',
        ),
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('920096bc-002e-4b62-a046-037e5ff87b31'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
