# Generated by Django 3.1.2 on 2021-02-25 08:01

import charities.validators
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
            name='Benefactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert')], default=0)),
                ('free_time_per_week', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=10, validators=[charities.validators.RegNumberValidator()])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('state', models.CharField(choices=[('P', 'Pending'), ('W', 'Waiting'), ('A', 'Assigned'), ('D', 'Done')], default='P', max_length=1)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('age_limit_from', models.IntegerField(blank=True, null=True)),
                ('age_limit_to', models.IntegerField(blank=True, null=True)),
                ('gender_limit', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('MF', 'Unset')], default='MF', max_length=2)),
                ('assigned_benefactor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='charities.benefactor')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charities.charity')),
            ],
        ),
    ]
