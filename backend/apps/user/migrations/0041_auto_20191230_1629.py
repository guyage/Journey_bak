# Generated by Django 2.0.4 on 2019-12-30 08:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_auto_20191230_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('2326a9cf-4ea3-41ca-ab50-fcef9c083936'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
