# Generated by Django 5.1.2 on 2024-10-22 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property_App', '0002_rename_units_unit_alter_property_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lease',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='units',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
        migrations.DeleteModel(
            name='Lease',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
