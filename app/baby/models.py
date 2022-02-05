from django.db import models
from django.utils import timezone

from app.base import BaseModel


class Baby(BaseModel):
    """婴儿信息"""
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=50, unique=True, verbose_name='名字')
    nickname = models.CharField(max_length=50, null=True, blank=True, verbose_name='小名')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='性别')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')

    def __str__(self):
        return f"{self.name}({self.nickname})"

    class Meta:
        db_table = 'baby'
        verbose_name = '婴儿信息'
        verbose_name_plural = verbose_name


class Growth(BaseModel):
    """生长记录"""
    baby = models.ForeignKey(to=Baby, related_name='baby_growth', on_delete=models.CASCADE, verbose_name='关联婴儿')
    height = models.FloatField(verbose_name='身高cm')
    weight = models.FloatField(verbose_name='体重kg')
    date = models.DateTimeField(default=timezone.now, verbose_name='记录时间')

    def __str__(self):
        return f"{self.baby}生长记录"

    class Meta:
        db_table = 'growth'
        verbose_name = '生长记录'
        verbose_name_plural = verbose_name


class Images(models.Model):
    image = models.ImageField(upload_to='static/photos/', blank=True, null=True)

    class Meta:
        db_table = 'images'
        verbose_name = '相册管理'
        verbose_name_plural = verbose_name


class LifeLog(BaseModel):
    """生活记录"""
    baby = models.ForeignKey(to=Baby, related_name='baby_life', on_delete=models.CASCADE, verbose_name='关联婴儿')
    content = models.TextField(verbose_name='记录正文')
    images = models.ManyToManyField(to=Images, related_name='images', verbose_name='照片')

    class Meta:
        db_table = 'life_log'
        verbose_name = '生活记录'
        verbose_name_plural = verbose_name
