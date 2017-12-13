#-*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,HiddenField, TextAreaField, SelectField, DecimalField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp
from flask.ext.uploads import UploadSet, IMAGES
from flask.ext.wtf.file import FileField, FileAllowed, FileRequired


images = UploadSet('images', IMAGES)


class PageInfo():
    def  __init__(self, pagename="", pagetask=""):
       self.pagename = pagename
       self.pagetask = pagetask


class SchoolForm(Form):
    id = HiddenField('id')
    name = StringField('學校名稱', validators=[Length(min=1, max= 50)]) # 學校名稱
    area_id = SelectField(u'所在區縣', coerce=int) #區縣
    teachdesc = TextAreaField(u'校長及教師情況') #
    address = StringField('位址') #
    schooltype_id = SelectField(u'學校型態', coerce=int) #
    website = StringField('網址') #
    distinguish = TextAreaField(u'教學特色') #
    leisure = TextAreaField(u'課外特色活動') #
    threashold = TextAreaField(u'招生條件及招生地塊') #
    partner = StringField('對口學校') #
    artsource = StringField('藝術特長招生情況') # 
    feedesc = StringField('學費標准') #
    longitude = DecimalField('經度', places=4)
    latitude =  DecimalField('緯度', places=4)
    feature_ids =  SelectMultipleField(u'教學特色', coerce=int)
    image = FileField('上傳圖片', validators= [FileAllowed(['jpg', 'png'], 'Images only!')])


class InstitutionForm(Form):
    id = HiddenField('id')
    name = StringField('品牌名', validators=[Length(min=1, max= 50)]) 
    agespan_id = SelectField(u'招生年齡', coerce=int)
    area_id = SelectField(u'所在區縣', coerce=int)
    address = StringField('位址') #
    location = StringField('校區名')
    website = StringField('網址') #
    telephone = StringField('電話')
    feedesc = StringField('學費標准') #
    timeopen = DateTimeField('開業時間', format='%H:%M')
    timeclose = DateTimeField('關門時間', format='%H:%M')
    feetype_id = SelectField('收費型態', coerce=int)
    longitude = DecimalField('經度', places=4)
    latitude =  DecimalField('緯度', places=4)
    #featuredesc = db.Column(db.String(200)) #特色小項描述
    feature_ids =  SelectMultipleField(u'教育訓練方向', coerce=int)
    image = FileField('上傳圖片', validators= [FileAllowed(['jpg', 'png'], 'Images only!')])


class BulletinForm(Form):
    id = HiddenField('id')
    dt = DateTimeField('發布時間', format = '%Y-%m-%d %H:%M:%S')
    title = StringField('標題')
    content = TextAreaField('詳情')
    valid = BooleanField('是否有效')
    source = StringField('來源')
    author =StringField('作者')
    image = FileField('上傳圖片', validators= [FileAllowed(['jpg', 'png'], 'Images only!')])


class AccountForm(Form):
    id = HiddenField('id')
    dtcreate = DateTimeField('登錄時間', format = '%Y-%m-%d %H:%M:%S')
    username = StringField('登入名')
    password = StringField('密碼')
    name = StringField('暱稱')
    telephone = StringField('登錄電話')
    flag_telephone = BooleanField('是否已認證')
    checkcode = StringField('認證碼')
    source = StringField('來源')
