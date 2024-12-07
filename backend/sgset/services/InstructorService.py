from rest_framework.exceptions import NotFound
from sgset.models import Instructor

class InstructorService:
    """
    Service class for managing InstructorModel instances.

    Provides methods for creating, retrieving, updating, and deleting Instructors.
    """

    @staticmethod
    def create_instructor(data):
        """
        Creates a new Instructor.

        Args:
            data (dict): A dictionary containing the Instructor data.

        Returns:
            InstructorModel: The newly created InstructorModel instance.

        Raises:
            KeyError: If any required key is missing in the input data.
        """
        try:
            return Instructor.objects.create(
                name=data['name'],
                source=data['source']
            )
        except KeyError as e:
            raise KeyError(f"Missing required field: {e}")


    @staticmethod
    def get_instructor(Instructor_id):
        """
        Retrieves a Instructor by its ID.

        Args:
            Instructor_id (UUID): The ID of the Instructor to retrieve.

        Returns:
            InstructorModel: The InstructorModel instance if found.

        Raises:
            NotFound: If no Instructor with the given ID exists.
        """
        try:
            return Instructor.objects.get(id=Instructor_id)
        except Instructor.DoesNotExist:
            raise NotFound(f"Instructor with ID {Instructor_id} not found.")

    @staticmethod
    def update_instructor(Instructor_id, data):
        """
        Updates an existing Instructor.

        Args:
            Instructor_id (UUID): The ID of the Instructor to update.
            data (dict): A dictionary containing the updated Instructor data.

        Returns:
            InstructorModel: The updated InstructorModel instance.

        Raises:
            NotFound: If no Instructor with the given ID exists.
        """
        Instructor = InstructorService.get_instructor(Instructor_id)
        for field, value in data.items():
             setattr(Instructor, field, value)  # Use setattr to dynamically update fields
        Instructor.save()
        return Instructor



    @staticmethod
    def delete_instructor(Instructor_id):
        """
        Deletes a Instructor.

        Args:
            Instructor_id (UUID): The ID of the Instructor to delete.

        Returns:
            None

        Raises:
            NotFound: If no Instructor with the given ID exists.
        """
        Instructor = InstructorService.get_instructor(Instructor_id)
        Instructor.delete()


    @staticmethod
    def list_instructors():
        """
        Lists all Instructors.

        Returns:
            QuerySet: A QuerySet of all InstructorModel instances.
        """
        return Instructor.objects.all()
