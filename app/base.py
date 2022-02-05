# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class BaseModel(models.Model):
    """模型基类"""
    create_user = models.IntegerField(default=None, null=True, verbose_name='创建人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_user = models.IntegerField(default=None, null=True, verbose_name='修改人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class BaseAdmin(admin.ModelAdmin):
    """Admin基类"""
    def save_model(self, request, obj, form, change):
        if change:
            obj.update_user = request.user.id
        else:
            obj.create_user = request.user.id
        obj.save()