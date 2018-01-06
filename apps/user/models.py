from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name = models.CharField('昵称', max_length=50, default='')
    birth = models.DateTimeField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=(('male','男'),('female','女')), default='male')
    address = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机号码', max_length=11, null=True, blank=True)
    avatar = models.ImageField('头像地址', max_length=100, upload_to='avatar/%Y/%m', default='avatar/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

