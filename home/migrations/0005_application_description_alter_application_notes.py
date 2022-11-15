# Generated by Django 4.0.8 on 2022-11-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_application_accepted_application_assessment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Job Description'),
        ),
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='notes'),
        ),
    ]
