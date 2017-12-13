# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Moment

class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("訊息內容", {
            'fields': ('content', 'kind')
        }),
        ('使用者訊息', {
            'fields': ('user_name',),
        }),
    )

class MyAdminSite(admin.AdminSite):
    site_header = '我的管理網站'

admin_site = MyAdminSite()
admin_site.register(Moment, MomentAdmin)
#admin.site.register(Moment, MomentAdmin)
