from django.contrib.auth import backends, get_user_model
from django.core.exceptions import ObjectDoesNotExist

UserModel = get_user_model()


class HashedPasswordAuthBackend(backends.ModelBackend):

    def authenticate(self, request, user_login=None, password=None, **kwargs):
        if user_login is None:
            user_login = kwargs.get(UserModel.USERNAME_FIELD)
        else:
            try:
                user = UserModel.objects.get(user_login=user_login)
                if user.password == password and self.user_can_authenticate(user):
                    return user
            except ObjectDoesNotExist:
                return False

        return super().authenticate(request, user_login, password, **kwargs)
