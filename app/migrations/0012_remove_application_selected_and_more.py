# Generated by Django 4.1.5 on 2023-04-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_application_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='selected',
        ),
        migrations.AddField(
            model_name='application',
            name='job_selection',
            field=models.CharField(choices=[('Selected ', ' Selected'), ('Pending', 'Pending'), ('Not Selected', 'Not Selected')], max_length=100, null=True),
        ),
    ]
