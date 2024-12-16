import pytest
from django.utils import timezone
from sgset.models import CourseClass, Course
from decimal import Decimal

@pytest.mark.django_db
@pytest.fixture
def course_instance():
    """Cria uma instância de Course para os testes."""
    return Course.objects.create(name="Mathematics")

@pytest.mark.django_db
@pytest.fixture
def course_class_instance(course_instance):
    """Cria uma instância de CourseClass para os testes."""
    return CourseClass.objects.create(
        code="CQ.AJUS.N-1",
        course=course_instance,
        shift="Evening",
        duration=30,
        modality="In-person",
        attendance="School",
        period_from=timezone.now().date(),
        period_to=timezone.now().date(),
        start_time=timezone.now().time(),
        end_time=timezone.now().time(),
        estimated_enrollments=40,
        actual_enrollments=35,
        quorum=20,
        status="programado",
        income=Decimal("1500.00")
    )

@pytest.mark.django_db
def test_course_class_creation(course_class_instance):
    """Teste a criação de uma instância de CourseClass."""
    course_class = course_class_instance
    assert course_class.code == "CQ.AJUS.N-1"
    assert course_class.course.name == "Mathematics"
    assert course_class.shift == "Evening"
    assert course_class.duration == 30
    assert course_class.modality == "In-person"
    assert course_class.attendance == "School"
    assert course_class.period_from is not None
    assert course_class.period_to is not None
    assert course_class.start_time is not None
    assert course_class.end_time is not None
    assert course_class.estimated_enrollments == 40
    assert course_class.actual_enrollments == 35
    assert course_class.quorum == 20
    assert course_class.status == "programado"
    assert course_class.income == Decimal("1500.00")
    
@pytest.mark.django_db
def test_course_class_str(course_class_instance):
    """Teste a string de representação do CourseClass."""
    course_class = course_class_instance
    assert str(course_class) == "CQ.AJUS.N-1 - Mathematics"
