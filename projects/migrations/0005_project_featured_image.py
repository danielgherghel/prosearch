# Generated by Django 4.0.6 on 2022-08-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_fetured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to=''),
        ),
    ]
