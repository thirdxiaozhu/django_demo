# Generated by Django 2.2.18 on 2021-05-14 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0061_auto_20210514_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='finishtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='gettime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
