# Generated by Django 5.1.1 on 2025-02-13 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_jobemployerprofile_vacancies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobemployerprofile',
            name='vacancy',
        ),
    ]
