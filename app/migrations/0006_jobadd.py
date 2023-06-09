# Generated by Django 4.1.7 on 2023-04-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_candidateuser_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_description', models.TextField(null=True)),
                ('job_type', models.CharField(choices=[('Full_Time', 'Full Time'), ('Part_Time', 'Part Time'), ('Contract', 'Contract'), ('Internship', 'Internship')], max_length=100, null=True)),
                ('industry', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('salary', models.CharField(max_length=100, null=True)),
                ('education_requirment', models.CharField(max_length=150, null=True)),
                ('experience_requirement', models.CharField(max_length=150, null=True)),
                ('skills_required', models.CharField(max_length=150, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]