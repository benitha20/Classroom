# Generated by Django 5.1.2 on 2024-10-21 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('number', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property_App.address')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property_App.address')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rent_amount', models.IntegerField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property_App.tenant')),
                ('units', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property_App.units')),
            ],
        ),
    ]
