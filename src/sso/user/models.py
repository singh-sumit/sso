import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from sso.user.managers import CustomUserManager


class User(AbstractBaseUser,PermissionsMixin):
    """
    Model to store all kind of user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)

    is_staff = models.BooleanField('staff status', default=False)
    is_active=models.BooleanField('active', default=True)
    date_joined=models.DateTimeField('date joined', auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'
        db_table='user'

    def __str__(self)->str:
        return f"<{self.__class__.__name__}> : {self.email}"
