# Generated by Django 2.2.18 on 2021-05-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0025_auto_20210508_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacherinfo',
            name='course',
            field=models.ManyToManyField(to='adminstrator.Course'),
        ),
    ]
