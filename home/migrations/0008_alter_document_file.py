# Generated by Django 4.0.8 on 2022-11-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_application_resume_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
