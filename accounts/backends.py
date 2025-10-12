from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    """Authenticate using email (entered as 'username' or via 'email' kwarg)."""
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        # choose the email candidate from either param
        if email is None:
            email = username
        if not email or password is None:
            return None

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user   # <-- correct indentation
        return None
