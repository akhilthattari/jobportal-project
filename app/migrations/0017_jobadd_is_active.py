# Generated by Django 4.1.7 on 2023-05-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_companyuser_registration_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadd',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
