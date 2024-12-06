from rest_framework.exceptions import NotFound
from sgset.models import InstructorClass

class InstructorClassService:
    """
    Service class for managing InstructorClassModel instances.

    Provides methods for creating, retrieving, updating, and deleting InstructorClasss.
    """

    @staticmethod
    def create_instructorclass(data):
        """
        Creates a new InstructorClass.

        Args:
            data (dict): A dictionary containing the InstructorClass data.

        Returns:
            InstructorClassModel: The newly created InstructorClassModel instance.

        Raises:
            KeyError: If any required key is missing in the input data.
        """
        try:
            return InstructorClass.objects.create(
                name=data['name'],
                source=data['source']
            )
        except KeyError as e:
            raise KeyError(f"Missing required field: {e}")


    @staticmethod
    def get_instructorclass(InstructorClass_id):
        """
        Retrieves a InstructorClass by its ID.

        Args:
            InstructorClass_id (UUID): The ID of the InstructorClass to retrieve.

        Returns:
            InstructorClassModel: The InstructorClassModel instance if found.

        Raises:
            NotFound: If no InstructorClass with the given ID exists.
        """
        try:
            return InstructorClass.objects.get(id=InstructorClass_id)
        except InstructorClass.DoesNotExist:
            raise NotFound(f"InstructorClass with ID {InstructorClass_id} not found.")

    @staticmethod
    def update_instructorclass(InstructorClass_id, data):
        """
        Updates an existing InstructorClass.

        Args:
            InstructorClass_id (UUID): The ID of the InstructorClass to update.
            data (dict): A dictionary containing the updated InstructorClass data.

        Returns:
            InstructorClassModel: The updated InstructorClassModel instance.

        Raises:
            NotFound: If no InstructorClass with the given ID exists.
        """
        InstructorClass = InstructorClassService.get_instructorclass(InstructorClass_id)
        for field, value in data.items():
             setattr(InstructorClass, field, value)  # Use setattr to dynamically update fields
        InstructorClass.save()
        return InstructorClass



    @staticmethod
    def delete_instructorClass(InstructorClass_id):
        """
        Deletes a InstructorClass.

        Args:
            InstructorClass_id (UUID): The ID of the InstructorClass to delete.

        Returns:
            None

        Raises:
            NotFound: If no InstructorClass with the given ID exists.
        """
        InstructorClass = InstructorClassService.get_instructorClass(InstructorClass_id)
        InstructorClass.delete()


    @staticmethod
    def list_instructorclass():
        """
        Lists all InstructorClasss.

        Returns:
            QuerySet: A QuerySet of all InstructorClassModel instances.
        """
        return InstructorClass.objects.all()
