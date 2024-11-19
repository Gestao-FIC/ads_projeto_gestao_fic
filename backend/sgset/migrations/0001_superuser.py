import uuid
import django
from decouple import config
from django.db import migrations
from django.db import models
from django.db.migrations.state import StateApps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

def create_initial_superuser(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    """Creates an initial superuser using environment variables.

    Args:
        apps (Apps): Django apps registry to get models dynamically.
        schema_editor (BaseDatabaseSchemaEditor): Allows schema alterations within migrations.
    
    Environment Variables:
        - DJANGO_SUPERUSER_USERNAME: Username of the superuser (default: 'admin').
        - DJANGO_SUPERUSER_EMAIL: Email of the superuser (default: 'admin@example.com').
        - DJANGO_SUPERUSER_PASSWORD: Password of the superuser (default: 'adminpassword').

    Returns:
        None
    """
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
        migrations.RunPython(create_initial_superuser)
    ]
