# Generated by Django 2.2.5 on 2020-11-11 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='NIK',
            new_name='nik',
        ),
    ]