# Generated by Django 2.0.4 on 2019-12-30 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20191230_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('c848fb31-c216-469b-bb39-4fcdb48988b2'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
