#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

PYTHONIOENCODING="UTF-8"

import os

if os.path.exists('sampleDB.db'):
    os.remove('sampleDB.db')

# 引入peewee套件的所有內容
from peewee import *

# 建立一個Sqlite資料庫引擎物件，該引擎開啟資料庫檔案sampleDB.db
db = SqliteDatabase("sampleDB.db")


# 定義一個ORM的基礎類別，在基礎類別中指定本ORM所使用的資料庫，
# 這樣在之後所有的子類別中就不用重復宣告資料庫
class BaseModel(Model):
    class Meta:
        database = db


# 定義course表，繼承自BaseModel
class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null=False)
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'course'  # 定義資料庫中的表名  # 定義 teacher 表，繼承自BaseModel

class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=False)
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field="id", related_name="course")

    class Meta:
        order_by = ('name',)
        db_table = "teacher"


# 建表，僅需建立一次
Course.create_table()
Teacher.create_table()
