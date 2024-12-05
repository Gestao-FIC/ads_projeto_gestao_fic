from drf_yasg import openapi
from rest_framework import status
from datetime import datetime

class GoalResponseSchema:
    """
    Defines the Swagger response schemas for Goal-related endpoints.
    """

    @staticmethod
    def get_goal_list_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="List of Goals",
                examples={"application/json": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "year": datetime.now().year,  
                        "goal_description": "Cursos",
                        "value": "50000.00"
                    },
                    {
                        "id": "223e4567-e89b-12d3-a456-426614174001",
                        "year": datetime.now().year,  
                        "goal_description": "Receita",
                        "value": "200000.00"
                    }
                ]}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

    @staticmethod
    def get_goal_detail_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="Goal Details",
                examples={"application/json": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "year": datetime.now().year,  
                    "goal_description": "Cursos",
                    "value": "50000.00"
                }}
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Goal not found",
                examples={"application/json": {"error": "Goal not found"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

    @staticmethod
    def create_goal_response_schema():
        return {
            status.HTTP_201_CREATED: openapi.Response(
                description="Goal created successfully",
                examples={"application/json": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "year": datetime.now().year,  
                    "goal_description": "Cursos",
                    "value": "50000.00"
                }}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

    @staticmethod
    def update_goal_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="Goal updated successfully",
                examples={"application/json": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "year": datetime.now().year,  
                    "goal_description": "Cursos",
                    "value": "60000.00"
                }}
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Goal not found",
                examples={"application/json": {"error": "Goal not found"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

    @staticmethod
    def delete_goal_response_schema():
        return {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Goal deleted successfully",
                examples={"application/json": {"message": "Goal deleted successfully"}}
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Goal not found",
                examples={"application/json": {"error": "Goal not found"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

