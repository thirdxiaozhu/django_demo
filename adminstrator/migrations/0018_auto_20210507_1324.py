# Generated by Django 2.2.18 on 2021-05-07 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0017_auto_20210507_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='outlook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator.Outlook'),
        ),
    ]
