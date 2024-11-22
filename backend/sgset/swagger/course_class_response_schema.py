from drf_yasg import openapi
from rest_framework import status

class CourseClassResponseSchema:
    @staticmethod
    def get_course_list_response_schema():
        return {
            status.HTTP_200_OK: openapi.Response(
                description="List of Course Classes",
                examples={"application/json": [
                    {
                        "code": "CQ.AJUS.N-1",
                        "course": 1,
                        "shift": "Morning",
                        "status": "programado",
                        "duration": 30,
                        "modality": "In-person",
                        "attendance": "School",
                        "period_from": "2024-11-20",
                        "period_to": "2024-11-20",
                        "start_time": "08:00",
                        "end_time": "10:00",
                        "estimated_enrollments": 25,
                        "actual_enrollments": 20,
                        "quorum": 15,
                        "income": "500.00"
                    }
                ]}
            ),
            status.HTTP_201_CREATED: openapi.Response(
                description="Course Class created successfully",
                examples={"application/json": {"message": "Course class created successfully"}}
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
                description="Course Class Details",
                examples={"application/json": {
                    "code": "CQ.AJUS.N-1",
                    "course": 1,
                    "shift": "Morning",
                    "status": "programado",
                    "duration": 30,
                    "modality": "In-person",
                    "attendance": "School",
                    "period_from": "2024-11-20",
                    "period_to": "2024-11-20",
                    "start_time": "08:00",
                    "end_time": "10:00",
                    "estimated_enrollments": 25,
                    "actual_enrollments": 20,
                    "quorum": 15,
                    "income": "500.00"
                }},
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Course class not found",
                examples={"application/json": {"error": "Course class not found"}}
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid data provided",
                examples={"application/json": {"error": "Invalid input data"}}
            ),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Course class deleted successfully",
                examples={"application/json": {"message": "Course class deleted successfully"}}
            ),
        }
