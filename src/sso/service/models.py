from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Service(models.Model):
    name = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50, unique=True)
    callback_url=models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='service'
        verbose_name='service'
        verbose_name_plural='services'


    def __str__(self)->str:
        return f"<{self.__class__.__name__}> : {self.identifier}"

    @classmethod
    def for_user(cls, user: USER) -> list:
        """Get all services the user has access to"""
        return cls.objects.filter(user_connections__user=user)

class Connection(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE,
                             related_name='service_connections')
    service=models.ForeignKey(Service, on_delete=models.CASCADE,
                              related_name='user_connections')

    class Meta:
        unique_together=('user', 'service')

    def __str__(self)->str:
        return f"<{self.__class__.__name__}>: {self.user} <-> {self.service.identifier}"