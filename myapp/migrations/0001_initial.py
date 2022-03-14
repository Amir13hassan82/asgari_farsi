# Generated by Django 4.0.3 on 2022-03-13 17:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=285)),
                ('last_name', models.CharField(max_length=285)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('age', models.PositiveIntegerField(max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('birth_date', models.DateField(default=datetime.datetime(2022, 3, 13, 17, 1, 5, 132311, tzinfo=utc))),
                ('address', models.TextField()),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('degree', models.CharField(choices=[('F', 'Freshman'), ('B', 'Bachelor'), ('M', 'master'), ('D', 'Doctor')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=285)),
                ('last_name', models.CharField(max_length=285)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('age', models.PositiveIntegerField(max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('birth_date', models.DateField(default=datetime.datetime(2022, 3, 13, 17, 1, 5, 132311, tzinfo=utc))),
                ('address', models.TextField()),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('degree', models.CharField(choices=[('F', 'Freshman'), ('B', 'Bachelor'), ('M', 'master'), ('D', 'Doctor')], default='F', max_length=1)),
                ('term', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=285)),
                ('last_name', models.CharField(max_length=285)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('age', models.PositiveIntegerField(max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('birth_date', models.DateField(default=datetime.datetime(2022, 3, 13, 17, 1, 5, 132311, tzinfo=utc))),
                ('address', models.TextField()),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('degree', models.CharField(choices=[('F', 'Freshman'), ('B', 'Bachelor'), ('M', 'master'), ('D', 'Doctor')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('F', 'Formal'), ('I', 'Informal')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('type', models.CharField(choices=[('A', 'Azad'), ('S', 'State'), ('N', 'Night')], default='S', max_length=1)),
                ('department', models.CharField(max_length=1)),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.boss')),
            ],
        ),
    ]