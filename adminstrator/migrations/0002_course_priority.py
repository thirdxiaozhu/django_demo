# Generated by Django 2.2.18 on 2021-04-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
