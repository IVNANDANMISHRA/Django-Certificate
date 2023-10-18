# Generated by Django 4.2.6 on 2023-10-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(to='assignment_app.student'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
