# -*- coding: utf-8 -*-
from django.core.mail import send_mail

FROM_EMAIL = 'huacnlee@foxmail.com'

MAIL_FOOT = u'''<br/><br/><br/>
Tmitter開發團隊.<br/>
<a href="http://www.tmitter.com">tmitter.com</a>'''

def send_regist_success_mail(userinfo):
    subject = u'登錄成功'
    body = u'''你好！<b>%s</b><br />
    你已經成功登錄成為Tmitter使用者<br />
    以下是您的訊息：<br />
    <ul>
        <li>使用者名稱：%s </li>
        <li>密碼:%s</li>
    </ul>''' % (userinfo['realname'],userinfo['username'],userinfo['password'])
    recipient_list= [userinfo['email']]    
    send(subject,body,recipient_list)

    
def send(subject,body,recipient_list):
    body += MAIL_FOOT
    send_mail(subject,body,FROM_EMAIL, recipient_list,fail_silently=True)     

def test(request):
    send_regist_success_mail(
        {
            'username' : 'huacnlee',
            'password' : '123123',
            'email' : 'huacn@qq.com',
            'realname' : 'Jason Lee',
        }
    )
