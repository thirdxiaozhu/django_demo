# Generated by Django 2.2.18 on 2021-04-28 15:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=18)),
                ('birthday', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=5)),
                ('kucun', models.IntegerField(default=1000)),
                ('maichu', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book')),
            ],
            options={
                'unique_together': {('author', 'book')},
            },
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(through='app01.Author2Book', to='app01.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetails'),
        ),
    ]