from ast import In
from enum import auto
from django.db import models
from django.db.models.fields import CharField, IntegerField, DateField, TextField
# Create your models here.

label_name = 'contentsapp'

class MeetupDB(models.Model):
    # primary key
    meet_board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30)

    # title : 게시글 제목
    # contents : 게시글 내용
    # meet_image_path : 게시글 이미지 저장 경로
    # meet_regi_date : 게시글 작성 날짜
    title = CharField(max_length=50)
    contents = TextField()
    meet_image_path = TextField()
    meet_regi_date = DateField()
    year = CharField(max_length=10)
    
    class Meta:
        db_table = 'meetup'
        app_label = label_name
        managed = False

class ProudDB(models.Model):
    # primary key
    proud_board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30)

    # title : 게시글 제목
    # contents : 게시글 내용
    # meet_image_path : 게시글 이미지 저장 경로
    # meet_regi_date : 게시글 작성 날짜
    title = CharField(max_length=50)
    contents = TextField()
    proud_image_path = TextField()
    proud_regi_date = DateField()
    year = CharField(max_length=10)

    class Meta:
        db_table = 'proud_board'
        app_label = label_name
        managed = False

class StudyDB(models.Model):
    # primary key
    study_board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30)

    # title : 게시글 제목
    # contents : 게시글 내용
    # meet_image_path : 게시글 이미지 저장 경로
    # meet_regi_date : 게시글 작성 날짜
    title = CharField(max_length=50)
    contents = TextField()
    category = CharField(max_length=30)
    link_url = TextField()
    study_regi_date = DateField()
    head_name = CharField(max_length=50)
    id_name = CharField(max_length=50)
    head_id_name = CharField(max_length=50)

    
    class Meta:
        db_table = 'study_board'
        app_label = label_name
        managed = False

class NoticeDB(models.Model):
    # primary key
    info_board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30)

    # title : 게시글 제목
    # contents : 게시글 내용
    # meet_image_path : 게시글 이미지 저장 경로
    # meet_regi_date : 게시글 작성 날짜
    title = CharField(max_length=50)
    contents = TextField()
    info_regi_date = DateField()
    head_name = CharField(max_length=50)
    id_name = CharField(max_length=50)
    head_id_name = CharField(max_length=50)

    class Meta:
        db_table = 'info_board'
        app_label = label_name
        managed = False

