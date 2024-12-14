import pytest
from sgset.models import DayOfWeek
import uuid


@pytest.mark.django_db
@pytest.fixture
def day_of_week_instance():
    return DayOfWeek.objects.create(name="Monday")


@pytest.mark.django_db
def test_day_of_week_creation(day_of_week_instance):
    day_of_week = day_of_week_instance
    assert isinstance(day_of_week.id, uuid.UUID)
    assert day_of_week.name == "Monday"


@pytest.mark.django_db
def test_day_of_week_str(day_of_week_instance):
    day_of_week = day_of_week_instance
    assert str(day_of_week) == "Monday"


@pytest.mark.django_db
def test_unique_day_of_week():
    DayOfWeek.objects.create(name="Tuesday")
    with pytest.raises(Exception):
        DayOfWeek.objects.create(name="Tuesday")
