from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):

    def _create_user(self, user_login, password=None):
        if not user_login:
            raise ValueError("Users must have an user_login")

        user = self.model(
            user_login=user_login,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_login, password):
        user = self._create_user(
            password=password,
            user_login=user_login,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def verifyAccount(self, user, user_input, code):
        if user_input == code:
            user.is_active = True
            user.save(using=self._db)
            return user
