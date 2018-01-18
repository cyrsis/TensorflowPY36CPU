#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

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
        db_table = 'course'  # 定義資料庫中的表名


# 定義 teacher 表，繼承自BaseModel
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

# 新增行
Course.create(id=1, title='經濟學', period=320, description='文理科學生均可選修')
Course.create(id=2, title='大學英語', period=300, description='大一學生必修課')
Course.create(id=3, title='哲學', period=100, description='必修課')
Course.create(id=104, title='編譯原理', period=100, description='電腦系選修')
Teacher.create(name='白陣君', gender=True, address='..', course_id=1)
Teacher.create(name='李森', gender=True, address='..', course_id=3)
Teacher.create(name='張雯雯', gender=False, address='..', course_id=2)

# 查詢一行
record = Course.get(Course.title == '大學英語')
print("課程：%s, 學時：%d" % (record.title, record.period))

# 更新
record.period = 200
record.save()

# 移除
record.delete_instance()

# 查詢所有記錄
courses = Course.select()
for i in courses:
    print(i.id, i.title, i.period, i.description)

# 帶條件查詢，並將結果按period字段倒序排序
courses = Course.select().where(Course.id < 10).order_by(Course.period.desc())
for i in courses:
    print(i.id, i.title, i.period, i.description)

# 統計所有課程的平均學時
total = Course.select(fn.Avg(Course.period).alias('avg_period'))
for i in total:
    print(u"平均學時：", i.avg_period)

# 更新多個記錄
Course.update(period=300).where(Course.id > 100).execute()

# 多表連線動作，Peewee會自動根據ForeignKeyField的外鍵定義進行連線：
Record = Course.select().join(Teacher).where(Teacher.gender == True)
for i in Record:
    print(i.id, i.title, i.period, i.description)
