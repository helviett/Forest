# Generated by Django 2.0.4 on 2018-05-24 06:15

import ForestSN.models.user_image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForestSN', '0004_auto_20180517_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='img',
            field=models.ImageField(upload_to=ForestSN.models.user_image.user_img_path),
        ),
    ]
