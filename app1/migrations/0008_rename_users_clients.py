# Generated by Django 4.0.6 on 2022-10-19 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_users_delete_phd_remove_profile_feedback_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Clients',
        ),
    ]