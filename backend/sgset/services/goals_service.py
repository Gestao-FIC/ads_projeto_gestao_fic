from rest_framework.exceptions import NotFound
from sgset.models import Goal

class GoalService:
    """
    Service class for managing GoalModel instances.

    Provides methods for creating, retrieving, updating, and deleting goals.
    """

    @staticmethod
    def create_goal(data):
        """
        Creates a new goal.

        Args:
            data (dict): A dictionary containing the goal data.

        Returns:
            GoalModel: The newly created GoalModel instance.

        Raises:
            KeyError: If any required key is missing in the input data.
        """
        try:
            return Goal.objects.create(
                year=data['year'],
                goal_description=data['goal_description'],
                value=data['value']
            )
        except KeyError as e:
            raise KeyError(f"Missing required field: {e}")


    @staticmethod
    def get_goal(goal_id):
        """
        Retrieves a goal by its ID.

        Args:
            goal_id (UUID): The ID of the goal to retrieve.

        Returns:
            GoalModel: The GoalModel instance if found.

        Raises:
            NotFound: If no goal with the given ID exists.
        """
        try:
            return Goal.objects.get(id=goal_id)
        except Goal.DoesNotExist:
            raise NotFound(f"Goal with ID {goal_id} not found.")

    @staticmethod
    def update_goal(goal_id, data):
        """
        Updates an existing goal.

        Args:
            goal_id (UUID): The ID of the goal to update.
            data (dict): A dictionary containing the updated goal data.

        Returns:
            GoalModel: The updated GoalModel instance.

        Raises:
            NotFound: If no goal with the given ID exists.
        """
        goal = GoalService.get_goal(goal_id)
        for field, value in data.items():
             setattr(goal, field, value)  # Use setattr to dynamically update fields
        goal.save()
        return goal



    @staticmethod
    def delete_goal(goal_id):
        """
        Deletes a goal.

        Args:
            goal_id (UUID): The ID of the goal to delete.

        Returns:
            None

        Raises:
            NotFound: If no goal with the given ID exists.
        """
        goal = GoalService.get_goal(goal_id)
        goal.delete()


    @staticmethod
    def list_goals():
        """
        Lists all goals.

        Returns:
            QuerySet: A QuerySet of all GoalModel instances.
        """
        return Goal.objects.all()
