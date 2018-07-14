from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        """
        Create and save user with the given email and password
        """

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        is_active = kwargs.pop('is_active', True)

        user = self.model(
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)
