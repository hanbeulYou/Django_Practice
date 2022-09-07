from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# admin site에 register한다
admin.site.register(User, UserAdmin)