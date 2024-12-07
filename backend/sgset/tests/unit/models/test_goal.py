import pytest
from sgset.models import Goal
from datetime import date
from decimal import Decimal
import uuid


@pytest.mark.django_db
@pytest.fixture
def goal_instance():
    return Goal.objects.create(
        year=2024,
        goal_description="cursos",
        value=Decimal("10000.00")
    )


@pytest.mark.django_db
def test_goal_creation(goal_instance):
    goal = goal_instance
    assert isinstance(goal.id, uuid.UUID)
    assert goal.year == 2024
    assert goal.goal_description == "cursos"
    assert goal.value == Decimal("10000.00")


@pytest.mark.django_db
def test_goal_str(goal_instance):
    goal = goal_instance
    assert str(goal) == "2024 - cursos: 10000.00"


@pytest.mark.django_db
def test_goal_unique_values():
    goal1 = Goal.objects.create(
        year=2024,
        goal_description="matriculas",
        value=Decimal("5000.00")
    )
    goal2 = Goal.objects.create(
        year=2024,
        goal_description="receita",
        value=Decimal("20000.00")
    )
    assert goal1.goal_description == "matriculas"
    assert goal2.goal_description == "receita"
    assert goal1.value == Decimal("5000.00")
    assert goal2.value == Decimal("20000.00")
