# Generated by Django 5.1.2 on 2024-10-18 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgset', '0003_days_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseclass',
            name='duration',
            field=models.IntegerField(null=True, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='actual_enrollments',
            field=models.IntegerField(null=True, verbose_name='Actual Enrollments'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='attendance',
            field=models.CharField(max_length=50, null=True, verbose_name='Attendance'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='estimated_enrollments',
            field=models.IntegerField(null=True, verbose_name='Estimated Enrollments'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='modality',
            field=models.CharField(max_length=50, null=True, verbose_name='Modality'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='period_from',
            field=models.DateField(null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='period_to',
            field=models.DateField(null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='shift',
            field=models.CharField(max_length=20, null=True, verbose_name='Shift'),
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='Start Time'),
        ),
    ]