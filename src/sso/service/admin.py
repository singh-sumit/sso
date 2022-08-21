from django.contrib import admin

# Register your models here.
from sso.service.models import Service, Connection

admin.site.register(
    [
        Service,
        Connection
    ]
)
