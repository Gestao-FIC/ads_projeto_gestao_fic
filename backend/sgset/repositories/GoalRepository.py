

from sgset.models.goal import GoalModel


class GoalRepository:
    """
    Repository to handle database operations for the GoalModel.
    """

    @staticmethod
    def get_all_goals():
        """
        Fetch all goals from the database.
        """
        return GoalModel.objects.all()

    @staticmethod
    def get_goal_by_id(goal_id):
        """
        Fetch a goal by its UUID.
        """
        return GoalModel.objects.filter(id=goal_id).first()

    @staticmethod
    def create_goal(data):
        """
        Create a new goal in the database.
        """
        return GoalModel.objects.create(**data)

    @staticmethod
    def update_goal(goal_id, data):
        """
        Update an existing goal by its UUID.
        """
        goal = GoalModel.objects.filter(id=goal_id).first()
        if goal:
            for key, value in data.items():
                setattr(goal, key, value)
            goal.save()
        return goal

    @staticmethod
    def delete_goal(goal_id):
        """
        Delete a goal by its UUID.
        """
        goal = GoalModel.objects.filter(id=goal_id).first()
        if goal:
            goal.delete()
        return goal
