from django.contrib import admin

from . import models


class LFLDailyInlineAdmin(admin.TabularInline):
    model = models.LFLDaily


@admin.register(models.LFL)
class LFLAdmin(admin.ModelAdmin):
    inlines = [LFLDailyInlineAdmin]


@admin.register(models.LFLDaily)
class LFLDailyAdmin(admin.ModelAdmin):
    pass
