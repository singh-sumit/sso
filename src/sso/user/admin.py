from django.contrib import admin

# Register your models here.
from sso.user.models import User

admin.site.register([
    User,
])