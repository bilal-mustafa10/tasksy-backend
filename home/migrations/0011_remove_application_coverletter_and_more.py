# Generated by Django 4.0.8 on 2022-11-14 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='coverLetter',
        ),
        migrations.RemoveField(
            model_name='application',
            name='offerLetter',
        ),
        migrations.RemoveField(
            model_name='application',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='application',
            name='recommendationLetter',
        ),
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='application',
            name='transcript',
        ),
        migrations.AddField(
            model_name='application',
            name='progress',
            field=models.CharField(max_length=200, null=True, verbose_name='Application Progress'),
        ),
        migrations.AlterField(
            model_name='application',
            name='accepted',
            field=models.BooleanField(null=True, verbose_name='Accepted'),
        ),
        migrations.AlterField(
            model_name='application',
            name='assessment',
            field=models.BooleanField(null=True, verbose_name='Assessment'),
        ),
        migrations.AlterField(
            model_name='application',
            name='deadline',
            field=models.DateField(null=True, verbose_name='Application Deadline'),
        ),
        migrations.AlterField(
            model_name='application',
            name='interviewCall',
            field=models.BooleanField(null=True, verbose_name='Interview Call'),
        ),
        migrations.AlterField(
            model_name='application',
            name='interviewFinal',
            field=models.BooleanField(null=True, verbose_name='Interview Final'),
        ),
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='application',
            name='offer',
            field=models.BooleanField(null=True, verbose_name='Offer'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.BooleanField(null=True, verbose_name='Application Status'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.FileField(upload_to='documents', verbose_name='file')),
                ('applicationId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.application')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]