# Generated by Django 4.1.1 on 2022-10-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit_api', '0004_remove_train_bearing_remove_train_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='location',
            field=models.JSONField(),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]