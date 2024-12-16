import pytest
from decimal import Decimal
from sgset.models import Course
import uuid


@pytest.mark.django_db
@pytest.fixture
def course_instance():
    """Cria uma instância de Course para os testes."""
    return Course.objects.create(
        name="Mechanical Fitter",
        price_per_student=Decimal("1200.00")
    )


@pytest.mark.django_db
def test_course_creation(course_instance):
    """Teste a criação de uma instância de Course."""
    course = course_instance
    assert isinstance(course.id, uuid.UUID)  # Verifica se o id é um UUID válido
    assert course.name == "Mechanical Fitter"
    assert course.price_per_student == Decimal("1200.00")


@pytest.mark.django_db
def test_course_str(course_instance):
    """Teste a string de representação do Course."""
    course = course_instance
    assert str(course) == "Mechanical Fitter - $1200.00"
    
@pytest.mark.django_db
def test_course_without_price():
    """Teste a criação de Course sem price_per_student."""
    course = Course.objects.create(
        name="Arduino"
    )
    assert course.name == "Arduino"
    assert course.price_per_student is None  # Preço não fornecido, deve ser None
