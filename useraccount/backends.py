from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

CustomUser = get_user_model()

class PhoneBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_number=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
        