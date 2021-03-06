# Generated by Django 2.2.18 on 2021-05-08 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0027_auto_20210508_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='ordinary', max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='form',
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=10, unique=True)),
                ('capacity', models.IntegerField()),
                ('function', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.Function')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='function',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.Function'),
        ),
    ]
