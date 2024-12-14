import pytest
from sgset.models import ClassSchedule, CourseClass, DayOfWeek, Course
from django.db.utils import IntegrityError

@pytest.mark.django_db  
@pytest.fixture
def course_instance():
    """Cria uma instância de Course para os testes."""
    return Course.objects.create(name="Inteligência Artificial") 

@pytest.mark.django_db
@pytest.fixture
def course_class_instance(course_instance):
    """Cria uma instância de CourseClassModel para os testes."""
    return CourseClass.objects.create(
        code="CS101", 
        course=course_instance  # Associando Course ao CourseClassModel
    )

@pytest.mark.django_db
@pytest.fixture
def day_of_week_instance():
    """Cria uma instância de DayOfWeekModel para os testes."""
    return DayOfWeek.objects.create(
        name="Segunda-Feira"  
    )

@pytest.mark.django_db
@pytest.fixture
def class_schedule_instance(course_class_instance, day_of_week_instance):
    """Cria uma instância de ClassScheduleModel para os testes."""
    return ClassSchedule.objects.create(
        class_instance=course_class_instance,
        day_of_week=day_of_week_instance
    )

@pytest.mark.django_db
def test_class_schedule_creation(class_schedule_instance):
    """Teste a criação de uma instância de ClassScheduleModel."""
    schedule = class_schedule_instance
    assert schedule.id is not None  # Verifica se o id foi gerado
    assert schedule.class_instance.code == "CS101"  # Verifica a classe associada
    assert schedule.day_of_week.name == "Segunda-Feira"  # Verifica o dia da semana associado

@pytest.mark.django_db
def test_class_schedule_str(class_schedule_instance):
    """Teste a representação em string de ClassScheduleModel."""
    schedule = class_schedule_instance
    expected_str = f'{schedule.class_instance} - {schedule.day_of_week.name}'
    assert str(schedule) == expected_str 

@pytest.mark.django_db
def test_class_schedule_associations(class_schedule_instance):
    """Teste as associações entre ClassScheduleModel e os modelos relacionados."""
    schedule = class_schedule_instance
    assert schedule.class_instance is not None  
    assert schedule.day_of_week is not None 

@pytest.mark.django_db
def test_class_schedule_without_class_instance():
    """Teste a criação de ClassScheduleModel sem class_instance."""
    with pytest.raises(IntegrityError): 
        ClassSchedule.objects.create(
            day_of_week=DayOfWeek.objects.first() 
        )

@pytest.mark.django_db
def test_class_schedule_without_day_of_week():
    """Teste a criação de ClassScheduleModel sem day_of_week."""
    with pytest.raises(IntegrityError): 
        ClassSchedule.objects.create(
            class_instance=CourseClass.objects.first() 
        )
