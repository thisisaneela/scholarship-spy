# Generated by Django 4.1.2 on 2022-11-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_rename_name_feedback_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='emoji',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
