from django.db import models
from django.utils import timezone

from app.baby.models import Baby
from app.base import BaseModel


class Eat(BaseModel):
    """进食管理"""
    eat_choices = (
        (0, '母乳亲喂'),
        (1, '母乳瓶喂'),
        (2, '配方奶')
    )
    baby = models.ForeignKey(to=Baby, related_name='baby_eat', on_delete=models.CASCADE, verbose_name='关联婴儿')
    eat_type = models.IntegerField(choices=eat_choices, default=0, verbose_name='喂养方式')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='开始时间')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='结束时间')
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return f"{self.baby}进食记录"

    class Meta:
        db_table = 'eat'
        verbose_name = '进食管理'
        verbose_name_plural = verbose_name


class Diaper(BaseModel):
    """尿布"""
    baby = models.ForeignKey(to=Baby, related_name='baby_diaper', on_delete=models.CASCADE, verbose_name='关联婴儿')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='开始时间')
    has_feces = models.BooleanField(default=False, verbose_name='是否有便便')
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return f"{self.baby}换尿布记录"

    class Meta:
        db_table = 'diaper'
        verbose_name = '尿布管理'
        verbose_name_plural = verbose_name


class Sleep(BaseModel):
    """睡眠"""
    baby = models.ForeignKey(to=Baby, related_name='baby_sleep', on_delete=models.CASCADE, verbose_name='关联婴儿')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='开始时间')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='结束时间')
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return f"{self.baby}睡眠记录"

    class Meta:
        db_table = 'sleep'
        verbose_name = '睡眠管理'
        verbose_name_plural = verbose_name
