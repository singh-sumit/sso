from django.contrib.auth.models import BaseUserManager
from django.apps.registry import apps

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with given credentials and user data.
        """
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")

        email = self.normalize_email(email)

        # Lookup the real model class from the global app registry so this manager
        # method can be used in migrations.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        user = GlobalUserModel(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
       Create and save a regular user with given credentials and user data.
       """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
