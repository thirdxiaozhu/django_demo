# Generated by Django 2.2.18 on 2021-05-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0005_auto_20210501_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
