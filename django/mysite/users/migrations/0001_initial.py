# Generated by Django 2.1.7 on 2019-04-22 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('pillar', models.CharField(default='', max_length=200)),
                ('type', models.CharField(default='', max_length=200)),
                ('class_related', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=200)),
                ('duration', models.CharField(default='', max_length=200)),
                ('assigned_professors', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('makeup', models.CharField(default='', max_length=200)),
                ('day', models.CharField(default='', max_length=200)),
                ('start', models.CharField(default='', max_length=200)),
                ('end', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=200)),
                ('pillar', models.CharField(default='', max_length=200)),
                ('code', models.CharField(default='', max_length=200)),
                ('term', models.CharField(default='', max_length=200)),
                ('core', models.CharField(default='', max_length=200)),
                ('subject_lead', models.CharField(default='', max_length=200)),
                ('cohort_size', models.CharField(default='', max_length=200)),
                ('cohorts', models.CharField(default='', max_length=200)),
                ('enrolment_size', models.CharField(default='', max_length=200)),
                ('cohorts_per_week', models.CharField(default='', max_length=200)),
                ('lectures_per_week', models.CharField(default='', max_length=200)),
                ('labs_per_week', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='module',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Module'),
        ),
    ]
