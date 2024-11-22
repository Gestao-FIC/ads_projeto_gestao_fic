from drf_yasg import openapi
from rest_framework import status


class CourseResponseSchema:
    """
    Defines the Swagger response schemas for CourseModel-related endpoints.
    """

    @staticmethod
    def get_course_list_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="List of Courses",
                examples={"application/json": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "name": "Mechanical Fitter",
                        "price_per_student": "150.00"
                    },
                    {
                        "id": "223e4567-e89b-12d3-a456-426614174001",
                        "name": "Arduino",
                        "price_per_student": "200.00"
                    }
                ]}
            ),
            status.HTTP_201_CREATED: openapi.Response(
                description="Course created successfully",
                examples={"application/json": {"message": "Course created successfully"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
        }

    @staticmethod
    def get_course_detail_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="Course Details",
                examples={"application/json": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "Mechanical Fitter",
                    "price_per_student": "150.00"
                }},
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Course not found",
                examples={"application/json": {"error": "Course not found"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Course deleted successfully",
                examples={"application/json": {"message": "Course deleted successfully"}}
            ),
        }
