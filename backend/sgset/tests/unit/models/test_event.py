import pytest
from sgset.models import EventModel
from sgset.models import Instructor
import uuid
from datetime import date


@pytest.mark.django_db
@pytest.fixture
def instructor_instance():
    return Instructor.objects.create(name="John Doe")


@pytest.mark.django_db
@pytest.fixture
def event_instance(instructor_instance):
    return EventModel.objects.create(
        instructor=instructor_instance,
        title="National Holiday",
        description="A national holiday",
        start_date=date(2024, 12, 25),
        end_date=date(2024, 12, 25),
        tag="feriado"
    )


@pytest.mark.django_db
def test_event_creation(event_instance):
    event = event_instance
    assert isinstance(event.id, uuid.UUID)
    assert event.title == "National Holiday"
    assert event.description == "A national holiday"
    assert event.start_date == date(2024, 12, 25)
    assert event.end_date == date(2024, 12, 25)
    assert event.tag == "feriado"
    assert event.instructor.name == "John Doe"


@pytest.mark.django_db
def test_event_str(event_instance):
    event = event_instance
    assert str(event) == "National Holiday (2024-12-25 - 2024-12-25)"


@pytest.mark.django_db
def test_event_unique_tag():
    instructor = Instructor.objects.create(name="Jane Doe")
    EventModel.objects.create(
        instructor=instructor,
        title="Holiday Event",
        start_date=date(2024, 12, 31),
        end_date=date(2024, 12, 31),
        tag="evento"
    )
    event = EventModel.objects.get(title="Holiday Event")
    assert event.tag == "evento"
