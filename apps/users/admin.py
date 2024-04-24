from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, GroupAdmin as DjangoGroupAdmin
from django.utils.translation import gettext_lazy as _
from apps.users import models

admin.site.unregister(Group)


@admin.register(models.GroupProxyModel)
class GroupAdmin(DjangoGroupAdmin):
    pass


@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "id", "username", "email", "first_name", "last_name", "middle_name", "is_active", "is_staff", "is_superuser"
    )
    list_display_links = ("id", "username")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
