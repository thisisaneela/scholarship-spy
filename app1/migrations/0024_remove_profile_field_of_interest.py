# Generated by Django 4.1.2 on 2022-11-03 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_profile_personal_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='field_of_interest',
        ),
    ]
