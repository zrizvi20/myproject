from django.contrib.auth.backends import ModelBackend
from users.models import User

class email_backend(object):
    def authenticate(self, username=None, password=None):
        try:
            user=User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        if check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
