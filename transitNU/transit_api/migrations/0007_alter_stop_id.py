# Generated by Django 4.1.1 on 2022-10-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit_api', '0006_line_stop_alter_train_line_alter_train_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
