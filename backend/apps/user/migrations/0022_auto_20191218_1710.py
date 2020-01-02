# Generated by Django 2.0.4 on 2019-12-18 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20191218_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('e570cdd2-b733-4bc7-89e6-6e9f8c499e3a'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
