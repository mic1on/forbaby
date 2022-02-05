from django.contrib import admin
from app.baby import models
from app.base import BaseAdmin


@admin.register(models.Baby)
class BabyAdmin(BaseAdmin):
    """婴儿"""
    fields = ('name', 'nickname', 'gender', 'birthday')
    list_display = ('name', 'nickname', 'gender', 'birthday')


@admin.register(models.Growth)
class GrowthAdmin(BaseAdmin):
    """生长记录"""
    fields = ('baby', 'height', 'weight', 'date')
    list_display = ('baby', 'height', 'weight')


@admin.register(models.LifeLog)
class LifeLogAdmin(BaseAdmin):
    """生活记录"""
    fields = ('baby', 'content', 'images')
    list_display = ('baby', 'content', 'create_time')
    filter_horizontal = ('images',)


@admin.register(models.Images)
class ImagesAdmin(BaseAdmin):
    """相册管理"""
    fields = ('image',)
    list_display = ('id', 'image')
