from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group as BaseGroup

from users.models import User, Group


admin.site.unregister(BaseGroup)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
