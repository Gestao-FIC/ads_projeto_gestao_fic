from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework.response import Response
from rest_framework.views import APIView

from sgset.serializers.AuthSerializer import AuthSerializer
from sgset.services.AuthService import AuthService

class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                token = AuthService.authenticate_user(username, password)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            except AuthenticationFailed as e:
                return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
