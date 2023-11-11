# Generated by Django 4.1.2 on 2022-11-01 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='institute',
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.profile')),
            ],
        ),
    ]
