from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=64)


# 用户登录记录表，供审计验证登录用
class UserLoginRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=50)
    userID = models.IntegerField()
    username = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
