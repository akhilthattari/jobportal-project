# Generated by Django 4.1.7 on 2023-04-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_candidateuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateuser',
            name='qualification',
            field=models.CharField(choices=[('High School', 'High School'), ('Higher Secondary', 'Higher Secondary'), ('DIPLOMA', 'DIPLOMA'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation'), ('PhD', 'PhD')], max_length=20, null=True),
        ),
    ]