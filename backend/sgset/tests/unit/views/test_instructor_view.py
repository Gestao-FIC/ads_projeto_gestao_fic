import pytest
from uuid import uuid4
from rest_framework import status
from sgset.models import Instructor


@pytest.mark.django_db
class TestInstructorListView:
    """
    Test cases for InstructorListView.
    """

    def test_get_instructors(self, client):
        """Test GET request to list all instructors."""
        # Setup: Cria dados no banco de teste
        Instructor.objects.create(name="John Doe", source="sgset")
        Instructor.objects.create(name="Jane Smith", source="user")

        # Action: Faz a requisição GET
        response = client.get('/instructor/')

        # Assertions
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Jane Smith"  # Verifica ordenação pelo nome

    def test_post_instructor_valid(self, client):
        """Test POST request to create a new instructor with valid data."""
        data = {'name': 'John Doe', 'source': 'sgset'}

        # Action: Faz a requisição POST
        response = client.post('/instructor/', data, format='json')

        # Assertions
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'John Doe'

        # Verifica se foi salvo no banco
        instructor = Instructor.objects.get(name='John Doe')
        assert instructor.source == 'sgset'

    def test_post_instructor_invalid(self, client):
        """Test POST request with invalid data."""
        data = {'name': ''}  # Dados inválidos

        # Action: Faz a requisição POST
        response = client.post('/instructor/', data, format='json')

        # Assertions
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'name' in response.data


# @pytest.mark.django_db
# class TestInstructorDetailView:
#     """
#     Test cases for InstructorDetailView.
#     """

#     def test_get_instructor_valid(self, client):
#         """Test GET request to retrieve a specific instructor."""
#         # Setup: Cria um instrutor
#         instructor = Instructor.objects.create(name="John Doe", source="sgset")

#         # Action: Faz a requisição GET
#         response = client.get(f'/instructors/{instructor.id}/')

#         # Assertions
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['name'] == "John Doe"

#     def test_get_instructor_not_found(self, client):
#         """Test GET request when the instructor is not found."""
#         # Action: Faz a requisição GET para um ID inexistente
#         response = client.get(f'/instructors/{uuid4()}/')

#         # Assertions
#         assert response.status_code == status.HTTP_404_NOT_FOUND

#     def test_put_instructor_valid(self, client):
#         """Test PUT request to update an instructor."""
#         # Setup: Cria um instrutor
#         instructor = Instructor.objects.create(name="John Doe", source="sgset")
#         data = {'name': 'John Updated', 'source': 'user'}

#         # Action: Faz a requisição PUT
#         response = client.put(f'/instructors/{instructor.id}/', data, format='json')

#         # Assertions
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['name'] == 'John Updated'

#         # Verifica se foi atualizado no banco
#         instructor.refresh_from_db()
#         assert instructor.name == 'John Updated'
#         assert instructor.source == 'user'

#     def test_put_instructor_invalid(self, client):
#         """Test PUT request with invalid data."""
#         # Setup: Cria um instrutor
#         instructor = Instructor.objects.create(name="John Doe", source="sgset")
#         data = {'name': ''}  # Dados inválidos

#         # Action: Faz a requisição PUT
#         response = client.put(f'/instructors/{instructor.id}/', data, format='json')

#         # Assertions
#         assert response.status_code == status.HTTP_400_BAD_REQUEST
#         assert 'name' in response.data

#     def test_delete_instructor_valid(self, client):
#         """Test DELETE request to remove an instructor."""
#         # Setup: Cria um instrutor
#         instructor = Instructor.objects.create(name="John Doe", source="sgset")

#         # Action: Faz a requisição DELETE
#         response = client.delete(f'/instructors/{instructor.id}/')

#         # Assertions
#         assert response.status_code == status.HTTP_204_NO_CONTENT

#         # Verifica se foi removido do banco
#         assert not Instructor.objects.filter(id=instructor.id).exists()

#     def test_delete_instructor_not_found(self, client):
#         """Test DELETE request for a non-existent instructor."""
#         # Action: Faz a requisição DELETE para um ID inexistente
#         response = client.delete(f'/instructors/{uuid4()}/')

#         # Assertions
#         assert response.status_code == status.HTTP_404_NOT_FOUND
