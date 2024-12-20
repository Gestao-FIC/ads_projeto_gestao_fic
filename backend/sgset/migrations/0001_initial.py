# Generated by Django 5.1.2 on 2024-12-06 00:01

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Course Name')),
                ('price_per_student', models.DecimalField(decimal_places=2,
                 max_digits=10, null=True, verbose_name='Price per Student')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('year', models.IntegerField(verbose_name='Year')),
                ('goal_description', models.CharField(choices=[('cursos', 'Cursos'), (
                    'matriculas', 'Matriculas'), ('receita', 'Receita')], max_length=12, verbose_name='Goal Type')),
                ('value', models.DecimalField(decimal_places=2,
                 max_digits=10, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(
                    max_length=100, verbose_name='Instructor Name')),
                ('source', models.CharField(choices=[
                 ('sgset', 'SGSET'), ('user', 'User')], max_length=10, verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True,
                 serialize=False, verbose_name='Class Code')),
                ('shift', models.CharField(
                    max_length=20, null=True, verbose_name='Shift')),
                ('duration', models.IntegerField(
                    null=True, verbose_name='Duration')),
                ('modality', models.CharField(
                    max_length=50, null=True, verbose_name='Modality')),
                ('attendance', models.CharField(
                    max_length=50, null=True, verbose_name='Attendance')),
                ('period_from', models.DateField(
                    null=True, verbose_name='Start Date')),
                ('period_to', models.DateField(null=True, verbose_name='End Date')),
                ('start_time', models.TimeField(
                    null=True, verbose_name='Start Time')),
                ('end_time', models.TimeField(null=True, verbose_name='End Time')),
                ('estimated_enrollments', models.IntegerField(
                    null=True, verbose_name='Estimated Enrollments')),
                ('actual_enrollments', models.IntegerField(
                    null=True, verbose_name='Actual Enrollments')),
                ('quorum', models.IntegerField(blank=True,
                 null=True, verbose_name='Minimum Quorum')),
                ('status', models.CharField(choices=[('programado', 'Programado'), ('em_andamento', 'Em andamento'), (
                    'concluido', 'Concluído'), ('cancelado', 'Cancelado')], max_length=12, verbose_name='Progress Status')),
                ('income', models.DecimalField(decimal_places=2, max_digits=10,
                 null=True, verbose_name='Income from Enrollments')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='classes', to='sgset.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Course Class',
                'verbose_name_plural': 'Course Classes',
                'ordering': ['period_from', 'start_time'],
            },
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_schedules', to='sgset.courseclass')),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_schedules', to='sgset.dayofweek')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(
                    blank=True, verbose_name='Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('tag', models.CharField(choices=[('feriado', 'Feriado'), ('emenda', 'Emenda'), ('evento', 'Evento'), ('curso', 'Curso'), ('outros', 'Outros')], max_length=10, verbose_name='Tag')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='sgset.instructor')),
            ],
            options={
                'verbose_name': 'Date Reservation',
                'verbose_name_plural': 'Date Reservations',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='InstructorClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructors', to='sgset.courseclass')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='sgset.instructor')),
            ],
            options={
                'verbose_name': 'Instructor Class',
                'verbose_name_plural': 'Instructor Class',
                'ordering': ['instructor', 'course_class'],
                'constraints': [models.UniqueConstraint(fields=('instructor', 'course_class'), name='unique_instructor_class')],
            },
        ),
    ]
