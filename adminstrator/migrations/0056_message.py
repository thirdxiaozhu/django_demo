# Generated by Django 2.2.18 on 2021-05-13 16:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0055_auto_20210513_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('gettime', models.DateField(default=django.utils.timezone.now)),
                ('finishtime', models.DateField(default=django.utils.timezone.now)),
                ('isFinished', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.AdminInfo')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.StudentInfo')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.TeacherInfo')),
            ],
        ),
    ]
