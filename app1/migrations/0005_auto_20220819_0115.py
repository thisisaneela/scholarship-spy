# Generated by Django 2.2.13 on 2022-08-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_scholarships_apply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='Apply_date',
            field=models.CharField(max_length=30),
        ),
    ]
