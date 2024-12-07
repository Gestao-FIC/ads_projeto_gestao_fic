import pytest
from sgset.models import ClassScheduleModel, CourseClassModel, DayOfWeekModel, CourseModel
from django.db.utils import IntegrityError

@pytest.mark.django_db  # Permite o acesso ao banco de dados durante o teste
@pytest.fixture
def course_instance():
    """Cria uma instância de Course para os testes."""
    return CourseModel.objects.create(name="Course 101")  # Supondo que o campo 'name' exista no modelo Course

@pytest.mark.django_db
@pytest.fixture
def course_class_instance(course_instance):
    """Cria uma instância de CourseClassModel para os testes."""
    return CourseClassModel.objects.create(
        code="CS101",  # Usando o campo 'code' que é esperado no modelo
        course=course_instance  # Associando Course ao CourseClassModel
    )

@pytest.mark.django_db
@pytest.fixture
def day_of_week_instance():
    """Cria uma instância de DayOfWeekModel para os testes."""
    return DayOfWeekModel.objects.create(
        name="Monday"  # Supondo que o modelo DayOfWeek tenha um campo 'name'
    )

@pytest.mark.django_db
@pytest.fixture
def class_schedule_instance(course_class_instance, day_of_week_instance):
    """Cria uma instância de ClassScheduleModel para os testes."""
    return ClassScheduleModel.objects.create(
        class_instance=course_class_instance,
        day_of_week=day_of_week_instance
    )

@pytest.mark.django_db
def test_class_schedule_creation(class_schedule_instance):
    """Teste a criação de uma instância de ClassScheduleModel."""
    schedule = class_schedule_instance
    assert schedule.id is not None  # Verifica se o id foi gerado
    assert schedule.class_instance.code == "CS101"  # Verifica a classe associada
    assert schedule.day_of_week.name == "Monday"  # Verifica o dia da semana associado

@pytest.mark.django_db
def test_class_schedule_str(class_schedule_instance):
    """Teste a representação em string de ClassScheduleModel."""
    schedule = class_schedule_instance
    expected_str = f'{schedule.class_instance} - {schedule.day_of_week.name}'
    assert str(schedule) == expected_str  # Verifica se o método __str__ retorna o valor esperado

@pytest.mark.django_db
def test_class_schedule_associations(class_schedule_instance):
    """Teste as associações entre ClassScheduleModel e os modelos relacionados."""
    schedule = class_schedule_instance
    assert schedule.class_instance is not None  # Verifica se a classe está associada
    assert schedule.day_of_week is not None  # Verifica se o dia da semana está associado

@pytest.mark.django_db
def test_class_schedule_without_class_instance():
    """Teste a criação de ClassScheduleModel sem class_instance."""
    with pytest.raises(IntegrityError):  # Espera-se que o Django lance um erro de integridade
        ClassScheduleModel.objects.create(
            day_of_week=DayOfWeekModel.objects.first()  # Usando um DayOfWeek válido
        )

@pytest.mark.django_db
def test_class_schedule_without_day_of_week():
    """Teste a criação de ClassScheduleModel sem day_of_week."""
    with pytest.raises(IntegrityError):  # Espera-se que o Django lance um erro de integridade
        ClassScheduleModel.objects.create(
            class_instance=CourseClassModel.objects.first()  # Usando um CourseClass válido
        )
