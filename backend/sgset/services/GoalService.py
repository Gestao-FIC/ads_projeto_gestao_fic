from repositories.GoalRepository import GoalRepository

class GoalService:
    """
    Service layer to handle business logic for goals.
    """

    @staticmethod
    def update_goal(goal_id, updates):
        """
        Update the goal and apply business logic.
        Business rule: Only updates the goal if the year is in the future.
        """
        goal = GoalRepository.get_goal_by_id(goal_id)
        if not goal:
            return None, "Goal not found."

        if goal.year < 2024:  
            return None, "Cannot update goals for past years."

        updated_goal = GoalRepository.update_goal(goal_id, updates)
        return updated_goal, "Goal updated successfully."
