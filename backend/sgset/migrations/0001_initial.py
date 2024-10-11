from django.db import migrations
from decouple import config

def create_initial_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username=config('DJANGO_SUPERUSER_USERNAME', default='admin'),
            email=config('DJANGO_SUPERUSER_EMAIL', default='admin@example.com'),
            password=config('DJANGO_SUPERUSER_PASSWORD', default='adminpassword')
        )

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.RunPython(create_initial_superuser),
    ]
