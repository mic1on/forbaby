from django.contrib import admin
from app.feed import models
from app.base import BaseAdmin


@admin.register(models.Eat)
class EatAdmin(BaseAdmin):
    """进食"""
    fields = ('baby', 'eat_type', 'start_time', 'end_time', 'remark')
    list_display = ('baby', 'eat_type', 'start_time', 'end_time')


@admin.register(models.Diaper)
class DiaperAdmin(BaseAdmin):
    """进食"""
    fields = ('baby', 'start_time', 'has_feces', 'remark')
    list_display = ('baby', 'start_time', 'has_feces')


@admin.register(models.Sleep)
class DiaperAdmin(BaseAdmin):
    """睡眠"""
    fields = ('baby', 'start_time', 'end_time', 'remark')
    list_display = ('baby', 'start_time', 'end_time')