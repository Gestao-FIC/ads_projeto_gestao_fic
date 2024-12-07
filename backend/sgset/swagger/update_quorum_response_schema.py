from drf_yasg import openapi
from rest_framework import status

class UpdateQuorumResponseSchema:
    @staticmethod
    def get_update_quorum_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="Quorum updated successfully",
                examples={"application/json": {"message": "Quorum updated successfully", "quorum": 20}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "The 'quorum' must be a positive integer."}}
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Course class not found",
                examples={"application/json": {"error": "Course class not found"}}
            ),
        }
