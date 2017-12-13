# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.  
KIND_CHOICES = (  
    ('Python技術', 'Python技術'),  
    ('資料庫技術', '資料庫技術'),  
    ('經濟學', '經濟學'),  
    ('文體資訊', '文體資訊'),  
    ('個人心情', '個人心情'),  
    ('其他', '其他'),  
)  

# Create your models here.
class Moment(models.Model):
    content = models.CharField(max_length=300, null=False)
    user_name = models.CharField(max_length = 20, default = '匿名')
    kind = models.CharField(max_length = 20, choices = KIND_CHOICES, default= KIND_CHOICES[0])
