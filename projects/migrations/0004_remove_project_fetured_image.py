# Generated by Django 4.0.6 on 2022-08-27 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_fetured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='fetured_image',
        ),
    ]
