from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

class UserRepository:

    @staticmethod
    def create_user(username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        return user

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound(detail="Usuário não encontrado.")

    @staticmethod
    def update_user(user, **kwargs):
        user.username = kwargs.get('username', user.username)
        user.email = kwargs.get('email', user.email)
        if 'password' in kwargs:
            user.set_password(kwargs['password'])
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()
        return {"detail": "Usuário excluído com sucesso."}
