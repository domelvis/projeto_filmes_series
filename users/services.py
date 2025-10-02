from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from users.models import UserActivity

User = get_user_model()

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def update_user_profile(user, data):
        """
        Atualiza o perfil do usuário com os dados fornecidos
        """
        fields_to_update = [
            'first_name', 'last_name', 'email', 
            'bio', 'email_notifications'
        ]
        
        for field in fields_to_update:
            if field in data:
                setattr(user, field, data[field])
        
        user.save()
        return user

    @staticmethod
    def update_user_password(user, current_password, new_password):
        """
        Atualiza a senha do usuário
        """
        if not user.check_password(current_password):
            return False, 'Senha atual incorreta'
            
        user.set_password(new_password)
        user.save()
        return True, 'Senha alterada com sucesso'

    @staticmethod
    def update_profile_image(user, image_file):
        """
        Atualiza a imagem de perfil do usuário
        """
        if user.profile_image:
            default_storage.delete(user.profile_image.path)
        
        user.profile_image = image_file
        user.save()
        return user

    @staticmethod
    def remove_profile_image(user):
        """
        Remove a imagem de perfil do usuário
        """
        if user.profile_image:
            default_storage.delete(user.profile_image.path)
            user.profile_image = None
            user.save()
        return user

    @staticmethod
    def delete_user_account(user):
        """
        Exclui a conta do usuário e todos os seus dados
        """
        if user.profile_image:
            default_storage.delete(user.profile_image.path)
        user.delete()
        return True

    @staticmethod
    def record_activity(user, activity_type, description):
        """
        Registra uma nova atividade do usuário
        """
        return UserActivity.objects.create(
            user=user,
            type=activity_type,
            description=description
        )

    @staticmethod
    def get_user_activities(user, limit=10):
        """
        Retorna as últimas atividades do usuário
        """
        return UserActivity.objects.filter(user=user).order_by('-created_at')[:limit]