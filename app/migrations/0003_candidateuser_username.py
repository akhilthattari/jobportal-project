# Generated by Django 4.1.7 on 2023-04-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_candidateuser_first_name_candidateuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateuser',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
