# Generated by Django 2.0.3 on 2018-03-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_logintemplates_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintemplates',
            name='pic',
            field=models.TextField(default=''),
        ),
    ]
