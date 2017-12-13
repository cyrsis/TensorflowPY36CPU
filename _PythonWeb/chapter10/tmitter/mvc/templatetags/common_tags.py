# -*- coding: utf-8 -*-
from django.template import Library
from tmitter.mvc.models import *
from tmitter.settings import *

register = Library()

def in_list(val,lst):
    """
    summary:
        檢查只時候在清單中
    author:
        Jason Lee
    """
    return val in lst

register.filter("in_list", in_list)