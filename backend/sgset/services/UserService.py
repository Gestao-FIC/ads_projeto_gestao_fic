from rest_framework.exceptions import NotFound

from sgset.repositories.UserRepository import UserRepository

class UserService:

    @staticmethod
    def create_user(data):
        return UserRepository.create_user(
            username=data['username'],
            email=data.get('email', ''),
            password=data['password']
        )

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = UserService.get_user(user_id)
        return UserRepository.update_user(
            user,
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )

    @staticmethod
    def delete_user(user_id):
        user = UserService.get_user(user_id)
        return UserRepository.delete_user(user)
