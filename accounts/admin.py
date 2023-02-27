from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

admin.site.register(Account)