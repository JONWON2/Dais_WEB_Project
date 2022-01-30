from ast import In
from enum import auto
from django.db import models
from django.db.models.fields import CharField, IntegerField, DateField, TextField
# Create your models here.

label_name = 'accountapp'
class User_info(models.Model):
    # primary key
    user_id = CharField(max_length=30, primary_key=True)

    # user_pw : 유저 패스워드
    # user_name : 유저 이름
    # user_email : 유저 이메일
    # user_phone : 유저 폰번호
    user_pw = CharField(max_length=30)
    user_name = CharField(max_length = 30)
    user_email = CharField(max_length=30)
    user_phone = CharField(max_length=30)

    class Meta:
        db_table = 'user'
        app_label = label_name
        managed = False