from django.contrib import admin

# Register your models here.

from .models import tb_user

admin.site.register(tb_user)