import uuid
from decouple import config
from django.db import migrations
from django.db import models
from django.db.migrations.state import StateApps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from sgset.models.day_of_week import DayOfWeek


def populate_days_of_week(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    """Populates the DayOfWeek table with standard days of the week (pt-br).

    Args:
        apps (StateApps): Django apps registry to get models dynamically.
        schema_editor (BaseDatabaseSchemaEditor): Allows schema alterations within migrations.

    Returns:
        None
    """
    days = [
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sabado"
    ]

    for day in days:
        if not DayOfWeek.objects.filter(name=day).exists():
            DayOfWeek.objects.create(id=uuid.uuid4(), name=day)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sgset', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(populate_days_of_week)
    ]
